from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

@login_required(login_url='loginUser')
def projects(request):
    searchQuery=''
    if request.GET.get('search_query'):
        searchQuery=request.GET.get('search_query')
    owner=Profile.objects.filter(name__icontains=searchQuery)
    project=Project.objects.filter(Q(title__icontains=searchQuery) | Q(owner__in=owner))
    context={'projects':project,'search_query':searchQuery}
    return(render(request,'projects.html',context))

def singleProject(request,pk):
    projectObj=Project.objects.get(id=pk) 
    tags=projectObj.tags.all()
    return(render(request,'singleProject.html',{'project':projectObj,'tags':tags}))

@login_required(login_url='loginUser')
def createProject(request):
    profile=request.user.profile
    form=ProjectForm
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            form.save()
            return redirect('projects')

    context={'form':form}
    return(render(request,'project_form.html',context))
@login_required(login_url='loginUser')
def updateProject(request,pk):
    form=ProjectForm
    profile=request.user.profile
    pro=profile.project_set.get(id=pk)
    form=ProjectForm(instance=pro)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context={'form':form}
    return(render(request,'project_form.html',context))

def deleteProject(request,pk):
    profile=request.user.profile
    pro=profile.project_set.get(id=pk)
    if request.method=='POST':
        print("getting deleted")
        pro.delete()
        return(redirect('projects'))

    return(render(request,'delete.html',{'project':pro}))

