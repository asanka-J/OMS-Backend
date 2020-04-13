from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Address

class UserForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
