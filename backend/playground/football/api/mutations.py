from django.forms import ModelForm
from graphene import Field, relay, ObjectType, String, Int, ID
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql import GraphQLError
from graphql_relay import from_global_id

from football.api.nodes import ManagerNode
from football.models import Manager


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'age']


class CreateManagerMutation(DjangoModelFormMutation, relay.ClientIDMutation):
    manager = Field(ManagerNode)

    class Meta:
        form_class = ManagerForm


class EditManagerMutation(relay.ClientIDMutation):

    class Input:
        manager = ID(required=True)
        first_name = String()
        last_name = String()
        age = Int()

    manager = Field(ManagerNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        global_id = input.get("manager")
        manager = Manager.objects.get(id=from_global_id(global_id)[1])

        if not manager:
            raise GraphQLError(f"Manager with id='{global_id}' not found")

        form = ManagerForm(
            data={
                'first_name': input.get("first_name", manager.first_name),
                'last_name': input.get("last_name", manager.last_name),
                'age': input.get("age", manager.age)
            },
            instance=manager
        )

        if form.is_valid():
            form.save()

        return EditManagerMutation(manager=manager)


class ManagerMutation(ObjectType):
    create_manager = CreateManagerMutation.Field()
    edit_manager = EditManagerMutation.Field()
