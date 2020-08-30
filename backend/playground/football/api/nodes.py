from graphene import relay, ID
from graphene_django import DjangoObjectType
from football.models import Manager, Stadium, Team, Competition, Player


class ManagerNode(DjangoObjectType):
    pk = ID(source="pk")

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
    pk = ID(source="pk")

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
    pk = ID(source="pk")

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
    pk = ID(source="pk")

    class Meta:
        model = Competition
        fields = ("id", "name", "format", "teams")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "format": ["exact"],
        }
        interfaces = (relay.Node,)


class PlayerNode(DjangoObjectType):
    pk = ID(source="pk")

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
