#all the urls will be configured here for the project

from django.urls import path
from django.contrib import admin 
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot')
    
]
