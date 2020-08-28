from django.forms import ModelForm
from graphene import relay, Field, ID, String, Int, ObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from football.api.mutations.util import update_instance, delete_instance
from football.api.nodes import ManagerNode
from football.models import Manager


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ["first_name", "last_name", "age"]


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
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("manager")
        manager = relay.Node.get_node_from_global_id(info, _id, only_type=ManagerNode)

        return cls(
            manager=update_instance(
                instance=manager, model_form=ManagerForm, data=input
            )
        )


class DeleteManagerMutation(relay.ClientIDMutation):
    class Input:
        manager = ID(required=True)

    manager = Field(ManagerNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("manager")
        manager = relay.Node.get_node_from_global_id(info, _id, only_type=ManagerNode)
        return cls(manager=delete_instance(instance=manager))


class ManagerMutation(ObjectType):
    create_manager = CreateManagerMutation.Field()
    edit_manager = EditManagerMutation.Field()
    delete_manager = DeleteManagerMutation.Field()
