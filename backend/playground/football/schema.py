import graphene
from graphene_django import DjangoObjectType
from football.models import Manager, Stadium, Team, Competition, Player


class ManagerNode(DjangoObjectType):
    class Meta:
        model = Manager
        fields = ("id", "first_name", "last_name", "age", "team")


class StadiumNode(DjangoObjectType):
    class Meta:
        model = Stadium
        fields = ("id", "name", "city", "capacity")


class TeamNode(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "country", "manager", "stadium", "player_set")


class CompetitionNode(DjangoObjectType):
    class Meta:
        model = Competition
        fields = ("id", "name", "format", "teams")


class PlayerNode(DjangoObjectType):
    class Meta:
        model = Player
        fields = ("id", "first_name", "last_name", "number", "age", "team")


def _get_object(model, id: int):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        return None


class FootballQuery(graphene.ObjectType):
    managers = graphene.List(ManagerNode)
    manager = graphene.Field(ManagerNode, id=graphene.Int(required=True))

    stadiums = graphene.List(StadiumNode)
    stadium = graphene.Field(StadiumNode, id=graphene.Int(required=True))

    teams = graphene.List(TeamNode)
    team = graphene.Field(TeamNode, id=graphene.Int(required=True))

    competitions = graphene.List(CompetitionNode)
    competition = graphene.Field(CompetitionNode, id=graphene.Int(required=True))

    players = graphene.List(PlayerNode)
    player = graphene.Field(PlayerNode, id=graphene.Int(required=True))

    def resolve_managers(self, _):
        return Manager.objects.all()

    def resolve_manager(self, _, id):
        return _get_object(Manager, id)

    def resolve_stadiums(self, _):
        return Stadium.objects.all()

    def resolve_stadium(self, _, id):
        return _get_object(Stadium, id)

    def resolve_teams(self, _):
        return Team.objects.all().select_related("stadium")

    def resolve_team(self, _, id):
        return _get_object(Team, id)

    def resolve_competitions(self, _):
        return Competition.objects.all().prefetch_related("teams")

    def resolve_compeition(self, _, id):
        return _get_object(Competition, id)

    def resolve_players(self, _):
        return Player.objects.all().select_related("team")

    def resolve_player(self, _, id):
        return _get_object(Player, id)
