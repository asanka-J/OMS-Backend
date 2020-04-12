import graphene
import graphql_jwt

# import links.schema
from .accounts.schema import (
    Query as userQuery,
    Mutation as userMutation
)
    


class Query(userQuery, graphene.ObjectType):
    pass


class Mutation(userMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)