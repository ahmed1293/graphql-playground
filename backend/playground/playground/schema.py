import graphene

from football.api.mutations import ManagerMutation
from football.api.query import FootballQuery


class Query(FootballQuery, graphene.ObjectType):
    pass


class Mutation(ManagerMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
