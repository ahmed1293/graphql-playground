from django.forms import ModelForm
from graphene import relay, Field, ID, String, Int, List, Enum, ObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from football.api.mutations.util import update_instance, delete_instance
from football.api.nodes import CompetitionNode
from football.models import Competition


class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'format', 'teams']


class FormatEnum(Enum):
    Knockout = Competition.KNOCKOUT
    League = Competition.LEAGUE


class CreateCompetitionMutation(DjangoModelFormMutation, relay.ClientIDMutation):
    competition = Field(CompetitionNode)

    class Meta:
        form_class = CompetitionForm


class EditCompetitionMutation(relay.ClientIDMutation):

    class Input:
        competition = ID(required=True)
        name = String()
        format = FormatEnum()
        teams = List(Int)

    competition = Field(CompetitionNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("competition")
        competition = relay.Node.get_node_from_global_id(info, _id, only_type=CompetitionNode)

        return cls(competition=update_instance(instance=competition, model_form=CompetitionForm, data=input))


class DeleteCompetitionMutation(relay.ClientIDMutation):
    class Input:
        competition = ID(required=True)

    competition = Field(CompetitionNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("competition")
        competition = relay.Node.get_node_from_global_id(info, _id, only_type=CompetitionNode)
        return cls(competition=delete_instance(instance=competition))


class CompetitionMutation(ObjectType):
    create_competition = CreateCompetitionMutation.Field()
    edit_competition = EditCompetitionMutation.Field()
    delete_competition = DeleteCompetitionMutation.Field()
