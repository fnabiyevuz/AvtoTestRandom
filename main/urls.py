from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('question/', question),
    path('view/', view),
    
    path('login/', Login),
    path('register/', register),
    path('logout/', LogOut),
]