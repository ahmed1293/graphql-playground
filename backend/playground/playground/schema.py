import graphene

from football.api.mutations.competition import CompetitionMutation
from football.api.mutations.manager import ManagerMutation
from football.api.mutations.player import PlayerMutation
from football.api.mutations.stadium import StadiumMutation
from football.api.mutations.team import TeamMutation
from football.api.query import FootballQuery


class Query(
    FootballQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    ManagerMutation,
    StadiumMutation,
    TeamMutation,
    CompetitionMutation,
    PlayerMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
