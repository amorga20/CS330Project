from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
# Render index.html
    vehicles = HowToUserVehicle.objects.all()
    print("Current Vehicle How To's", vehicles)
    return render( request, 'how_to_app/index.html')

class HowToUserVehicleListView(generic.ListView):
    model = HowToUserVehicle

class HowToUserVehicleDetailView(generic.DetailView):
    model = HowToUserVehicle

    #def get_context_data(self, **kwargs):
        #context = super(HowToUserVehicleDetailView, self).get_context_data(**kwargs)
        #vehicle = HowToUserVehicle.objects.filter(id=self.object)
        #context["vehicle"] = vehicle
        #return context

# Def to create a project
def createProject(request):
    form = VehicleForm()
    #vehicle = HowToUser.objects.get(pk=howToUser_id)

    if request.method == "POST":
        # Create a new dictionary with form data and portfolio_id
        vehicle_data = request.POST.copy()
        #vehicle_data["vehicle_id"] = howToUser_id

        form = VehicleForm(vehicle_data)
        if form.is_valid():
            # Save the form without committing to the database
            vehicle = form.save(commit=False)
            # Set the portfolio relationship
            vehicle.howToUser = vehicle
            vehicle.save()

            # Redirect back to the portfolio detail page
            return redirect("index")

    context = {"form": form}
    return render(request, "how_to_app/howToUser_form.html", context)


# Def to delete a project
def deleteProject(request, pk):
    # Retrieve the project object or return a 404 response if it doesn't exist
    vehicle = get_object_or_404(HowToUserVehicle, id=pk)

    if request.method == "POST":
        if request.POST.get("confirm") == "yes":
            # If the request method is POST, it's a confirmation to delete
            vehicle.delete()

            # Redirect to the portfolio page after deletion
            return redirect("vehicles")

        elif request.POST.get("cancel") == "yes":
            # If the user "cancel" the deletion then go back to the portfolio page
            return redirect("vehicle-detail", pk)

    # If the request method is not POST, render a confirmation page
    context = {"project": vehicle}
    return render(request, "how_to_app/project_delete.html", context=context)


def updateProject(request, pk):
    # Get the project object based on its primary key (project_id)
    vehicle = get_object_or_404(HowToUserVehicle, id=pk)

    # Check if the request method is POST
    if request.method == "POST":
        # Create a ProjectForm instance
        form = VehicleForm(request.POST, instance=vehicle)
        # Check if the form data is valid
        if form.is_valid():
            # If the form is valid, save the changes to the project
            form.save()
            # Go back to the portfolio detail page
            return redirect("vehicle-detail", pk)
    else:
        # If the request method is not POST, create a form with the project data
        form = VehicleForm(instance=vehicle)

        return render(
            request,
            "how_to_app/project_update.html",
            {"form": form, "project": vehicle},
        )

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='model')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context ={'form':form}
    return render(request, 'registration/register.html', context)
