""" Motor Data  URLs."""

# Django
from django.urls import path

# Views
from motorDataApp import views

urlpatterns = [
    # API Overview
    path(
    	route='',
    	view= views.apiOverview,
    	name='overview'
    ),
    # Motor available data List
    path(
        route='motorData-List',
        view= views.motorDataList,
        name='motorDataList'
    ),

]	