from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
# Render index.html
    return render( request, 'how_to_app/index.html')
