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
        route='motorData-list',
        view= views.motorDataList,
        name='motorDataList'
    ),

    # Motor detail
    path(
        route='motor-detail/<str:pk>/',
        view= views.motorDetail,
        name='motorDetail'
    ),

    # Create motor data
    path(
        route='motor-create/',
        view= views.motorCreate,
        name='motorCreate',
    ),

    # Update motor data
    path(
        route='motor-update/<str:pk>/',
        view= views.motorUpdate,
        name='motorUpdate',
    ),

    # Delete motor data
    path(
        route='motor-delete/<str:pk>/',
        view= views.motorDelete,
        name='motorDelete',
    ),

]	