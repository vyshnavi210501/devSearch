from django.urls import path
from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('',getProfiles),
    path('add',addData),
    path('<str:pk>',getProfile),
    path('<str:pk>/pro',getProject),
    path('/projects/',getProjects),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:pk>/projectVote',getProjectVote),
]