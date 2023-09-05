from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # from file views connect template index
]
