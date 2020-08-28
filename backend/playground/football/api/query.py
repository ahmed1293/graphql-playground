from graphene import ObjectType, relay, Int
from graphene_django.filter import DjangoFilterConnectionField

from football.api.nodes import (
    ManagerNode,
    StadiumNode,
    TeamNode,
    CompetitionNode,
    PlayerNode,
)
from football.models import Manager, Stadium, Team, Competition, Player


def _get_object(model, _id: int):
    try:
        return model.objects.get(id=_id)
    except model.DoesNotExist:
        return None


class FootballQuery(ObjectType):
    managers = DjangoFilterConnectionField(ManagerNode)
    manager = relay.Node.Field(ManagerNode, id=Int(required=True))

    stadiums = DjangoFilterConnectionField(StadiumNode)
    stadium = relay.Node.Field(StadiumNode, id=Int(required=True))

    teams = DjangoFilterConnectionField(TeamNode)
    team = relay.Node.Field(TeamNode, id=Int(required=True))

    competitions = DjangoFilterConnectionField(CompetitionNode)
    competition = relay.Node.Field(CompetitionNode, id=Int(required=True))

    players = DjangoFilterConnectionField(PlayerNode)
    player = relay.Node.Field(PlayerNode, id=Int(required=True))

    def resolve_manager(self, _, id):
        return _get_object(Manager, id)

    def resolve_stadium(self, _, id):
        return _get_object(Stadium, id)

    def resolve_team(self, _, id):
        return _get_object(Team, id)

    def resolve_compeition(self, _, id):
        return _get_object(Competition, id)

    def resolve_player(self, _, id):
        return _get_object(Player, id)
