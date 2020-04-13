from django.contrib.auth import get_user_model
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...accounts.forms import UserForm,AddressForm

import graphene
from graphene_django import DjangoObjectType
from ...accounts.models import Address

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class CreateUserFMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)
    class Meta:
        form_class = UserForm
       
class CreatAddressFMutation(DjangoModelFormMutation):
    address = graphene.Field(AddressType)
    class Meta:
        form_class = AddressForm

class CreatevendorFMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)
    class Meta:
        form_class = UserForm
        


# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserType)

#     class Arguments:
#         # firstname = graphene.String(required=True)
#         password = graphene.String(required=True)
#         email = graphene.String(required=True)

#     def mutate(self, info, password, email):
#         user = get_user_model()(
#             email=email,
#         )
#         user.set_password(password)
#         user.save()

#         return CreateUser(user=user)


# class CreateAddress(graphene.Mutation):
#     address = graphene.Field(AddressType)

#     class Arguments:
#         # firstname = graphene.String(required=True)
#         password = graphene.String(required=True)
#         email = graphene.String(required=True)
#         first_name =  graphene.String(required=True)
#         last_name =  graphene.String(required=False)
#         # company_name = models.CharField(max_length=256, blank=True)
#         street_address_1 =  graphene.String(required=False)
#         street_address_2 = graphene.String(required=False)
#         city = graphene.String(required=False)
#         city_area =  graphene.String(required=False)
#         postal_code =  graphene.String(required=False)
#         country = graphene.String(required=False)
#         # country_area = models.CharField(max_length=128, blank=True)
#         phone = graphene.String(required=False)

#     def mutate(self, info, password, email):
#         user = get_user_model()(
#             email=email,
#         )
#         user.set_password(password)
#         user.save()

#         return CreateUser(user=user)

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType) 
    address = graphene.List(AddressType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_user(self, info, email):
        return get_user_model().objects.filter(email=email).first()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user
    
    def resolve_address(self, info, **kwargs):
        return Address.objects.all()


class Mutation(graphene.ObjectType):
    # create_user = CreateUser.Field()
    # create_address = CreateAddress.Field()
    createUser = CreateUserFMutation.Field()
    createAddress = CreatAddressFMutation.Field()
