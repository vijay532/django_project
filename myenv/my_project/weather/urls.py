#The difference is that this urls.py file contains all the URLs that are relevant to the app itself.

from django.urls import path 
from . import views 
urlpatterns = [
path('', views.index),
]

