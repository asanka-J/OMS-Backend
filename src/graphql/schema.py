import graphene
import graphql_jwt

# import links.schema
from .accounts.schema import (
    Query as accountsQuery,
    Mutation as accountsMutation
)

from .product.schema import (
    Query as productQuery,
    Mutation as productutation
)
    


class Query(accountsQuery, productQuery, graphene.ObjectType):
    pass


class Mutation(accountsMutation, productutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)