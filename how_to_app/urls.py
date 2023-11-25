from django.urls import path, include
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('vehicle/', views.HowToUserVehicleListView.as_view(), name='vehicles'),
    path('vehicle/<int:pk>', views.HowToUserVehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle/create_project/', views.createProject, name='create_project'),
    # Delete
    path("vehicle/<int:pk>/delete/", views.deleteProject, name="delete_project"),
    # Update Project
    path("vehicle/<int:pk>/update/", views.updateProject, name="update_project"),
    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name = 'register_page'),
]
