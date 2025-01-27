from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.singleProject,name='project'),
    path('create-project/',views.createProject,name='createProject'),
    path('update-project/<str:pk>/',views.updateProject,name='updateProject'),
    path('delete-project/<str:pk>/',views.deleteProject,name='deleteProject')
]