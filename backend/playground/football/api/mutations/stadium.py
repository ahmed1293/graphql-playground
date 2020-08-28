from django.forms import ModelForm
from graphene import relay, Field, ID, String, Int, ObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from football.api.mutations.util import update_instance, delete_instance
from football.api.nodes import StadiumNode
from football.models import Stadium


class StadiumForm(ModelForm):
    class Meta:
        model = Stadium
        fields = ["name", "city", "capacity"]


class CreateStadiumMutation(DjangoModelFormMutation, relay.ClientIDMutation):
    stadium = Field(StadiumNode)

    class Meta:
        form_class = StadiumForm


class EditStadiumMutation(relay.ClientIDMutation):
    class Input:
        stadium = ID(required=True)
        name = String()
        city = String()
        capacity = Int()

    stadium = Field(StadiumNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("stadium")
        stadium = relay.Node.get_node_from_global_id(info, _id, only_type=StadiumNode)

        return cls(
            stadium=update_instance(
                instance=stadium, model_form=StadiumForm, data=input
            )
        )


class DeleteStadiumMutation(relay.ClientIDMutation):
    class Input:
        stadium = ID(required=True)

    stadium = Field(StadiumNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("stadium")
        stadium = relay.Node.get_node_from_global_id(info, _id, only_type=StadiumNode)
        return cls(stadium=delete_instance(instance=stadium))


class StadiumMutation(ObjectType):
    create_stadium = CreateStadiumMutation.Field()
    edit_stadium = EditStadiumMutation.Field()
    delete_stadium = DeleteStadiumMutation.Field()
