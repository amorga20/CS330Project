from django.forms import ModelForm
from .models import *

#create class for project form

class VehicleForm(ModelForm):
    class Meta:
        model = HowToUserVehicle
        fields = ["year", "make", "model"]