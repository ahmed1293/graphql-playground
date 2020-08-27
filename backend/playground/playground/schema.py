import graphene
from football.schema import FootballQuery


class Query(FootballQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
