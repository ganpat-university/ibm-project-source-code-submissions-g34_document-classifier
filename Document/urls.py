from os import name
from django.urls import path,include
from django.urls.resolvers import URLPattern 
from .views import *

urlpatterns = [
    path('', home, name = "home" ),
    path('contact/', contact,name = "contact"),
    path('upload/', upload, name = "upload"),
]