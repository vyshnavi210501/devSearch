from django.urls import path
from .views import *

urlpatterns = [
    path('',getProfiles),
    path('add',addData),
    path('<str:pk>',getProfile),
]