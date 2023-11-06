from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import *
from .forms import *


# Create your views here.
def index(request):
# Render index.html
    return render( request, 'how_to_app/index.html')

class HowToUserVehicleListView(generic.ListView):
    model = HowToUserVehicle

class HowToUserVehicleDetailView(generic.DetailView):
    model = HowToUserVehicle



    
