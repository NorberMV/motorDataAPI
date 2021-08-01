""" Motor Data  URLs."""

# Django
from django.urls import path

# Views
from motorDataApp import views

urlpatterns = [
    # API URLs list
    path(
    	route='motor-list/',
    	view= views.apiOverview,
    	name='list'
    ),

]	