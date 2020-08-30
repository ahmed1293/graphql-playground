from django.forms import ModelForm
from graphene import relay, Field, ID, String, Int, List, Enum, ObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from football.api.mutations.util import update_instance, delete_instance
from football.api.nodes import PlayerNode
from football.models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'number', 'age', 'team']


class CreatePlayerMutation(DjangoModelFormMutation, relay.ClientIDMutation):
    player = Field(PlayerNode)

    class Meta:
        form_class = PlayerForm


class EditPlayerMutation(relay.ClientIDMutation):

    class Input:
        player = ID(required=True)
        first_name = String()
        last_name = String()
        number = Int()
        age = Int()
        team = Int()

    player = Field(PlayerNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("player")
        player = relay.Node.get_node_from_global_id(info, _id, only_type=PlayerNode)

        return cls(player=update_instance(instance=player, model_form=PlayerForm, data=input))


class DeletePlayerMutation(relay.ClientIDMutation):
    class Input:
        player = ID(required=True)

    player = Field(PlayerNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("player")
        player = relay.Node.get_node_from_global_id(info, _id, only_type=PlayerNode)
        return cls(player=delete_instance(instance=player))


class PlayerMutation(ObjectType):
    create_player = CreatePlayerMutation.Field()
    edit_player = EditPlayerMutation.Field()
    delete_player = DeletePlayerMutation.Field()
