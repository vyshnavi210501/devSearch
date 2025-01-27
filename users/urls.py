from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginUser,name='loginUser'),
    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.userProfile,name='userProfile'),
    path('logout/',views.logoutUser,name='logoutUser'),
    path('register/',views.registerUser,name='registerUser'),
    path('account/',views.userAccount,name='userAccount'),
    path('editAccount/',views.editAccount,name='edit-account'),
    path('create-skill/',views.createSkill,name='create-skill'),
    path('update-skill/<str:pk>/',views.updateSkill,name='update-skill'),
    path('delete-skill/<str:pk>/',views.deleteSkill,name='delete-skill'),
]