from django.forms import ModelForm
from graphene import relay, Field, ID, String, Int, ObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from football.api.mutations.util import update_instance, delete_instance
from football.api.nodes import TeamNode
from football.models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "country", "manager", "stadium"]


class CreateTeamMutation(DjangoModelFormMutation, relay.ClientIDMutation):
    team = Field(TeamNode)

    class Meta:
        form_class = TeamForm


class EditTeamMutation(relay.ClientIDMutation):
    class Input:
        team = ID(required=True)
        name = String()
        country = String()
        manager = Int()
        stadium = Int()

    team = Field(TeamNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("team")
        team = relay.Node.get_node_from_global_id(info, _id, only_type=TeamNode)

        return cls(team=update_instance(instance=team, model_form=TeamForm, data=input))


class DeleteTeamMutation(relay.ClientIDMutation):
    class Input:
        team = ID(required=True)

    team = Field(TeamNode)

    @classmethod
    def mutate_and_get_payload(cls, _, info, **input):
        _id = input.get("team")
        team = relay.Node.get_node_from_global_id(info, _id, only_type=TeamNode)
        return cls(team=delete_instance(instance=team))


class TeamMutation(ObjectType):
    create_team = CreateTeamMutation.Field()
    edit_team = EditTeamMutation.Field()
    delete_team = DeleteTeamMutation.Field()
