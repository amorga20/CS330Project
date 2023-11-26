from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form

class VehicleForm(ModelForm):
    class Meta:
        model = HowToUserVehicle
        fields = ["year", "make", "model"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class HowToUserForm(ModelForm):
    class Meta:
        model = HowToUser
        fields = '__all__'
        exclude =['user']