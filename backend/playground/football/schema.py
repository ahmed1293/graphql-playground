from graphene import relay, ObjectType, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from football.models import Manager, Stadium, Team, Competition, Player


class ManagerNode(DjangoObjectType):
    class Meta:
        model = Manager
        fields = ("id", "first_name", "last_name", "age", "team")
        filter_fields = {
            "first_name": ["exact", "icontains", "istartswith"],
            "last_name": ["exact", "icontains", "istartswith"],
            "age": ["exact", "gte", "lte"],
        }
        interfaces = (relay.Node,)


class StadiumNode(DjangoObjectType):
    class Meta:
        model = Stadium
        fields = ("id", "name", "city", "capacity")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "city": ["exact", "icontains"],
            "capacity": ["exact", "gte", "lte"],
        }
        interfaces = (relay.Node,)


class TeamNode(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "country", "manager", "stadium", "player_set")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact", "icontains"],
            "manager": ["exact"],
        }
        interfaces = (relay.Node,)


class CompetitionNode(DjangoObjectType):
    class Meta:
        model = Competition
        fields = ("id", "name", "format", "teams")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "format": ["exact"],
        }
        interfaces = (relay.Node,)


class PlayerNode(DjangoObjectType):
    class Meta:
        model = Player
        fields = ("id", "first_name", "last_name", "number", "age", "team")
        filter_fields = {
            "first_name": ["exact", "icontains", "istartswith"],
            "last_name": ["exact", "icontains", "istartswith"],
            "number": ["exact", "gte", "lte"],
            "age": ["exact", "gte", "lte"],
            "team": ["exact"],
        }
        interfaces = (relay.Node,)


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
