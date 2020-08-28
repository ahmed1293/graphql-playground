import graphene

from football.api.mutations.manager import ManagerMutation
from football.api.mutations.stadium import StadiumMutation
from football.api.mutations.team import TeamMutation
from football.api.query import FootballQuery


class Query(FootballQuery, graphene.ObjectType):
    pass


class Mutation(ManagerMutation, StadiumMutation, TeamMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
