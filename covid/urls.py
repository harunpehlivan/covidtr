from django.urls import path, include
from .views import *

urlpatterns = [  
    path('', index, name="index"),
    path('country/<str:country>/', country)
]