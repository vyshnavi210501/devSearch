from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm,ProfileForm,SkillForm
from django.db.models import Q
from .utils import searchProfiles

# Create your views here.
def loginUser(request):
    page='login'
    context={'page':page}
    if request.user.is_authenticated:
        return(redirect('profiles'))
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exists")
                  
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return(redirect('profiles'))
        else:
            messages.error(request,"Username or Password is incorrect")

    return(render(request,'login_register.html',context))

def logoutUser(request):
    logout(request)
    return(redirect('loginUser'))

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)


def profiles(request):
    pro,searchQuery=searchProfiles(request)
    context={'profiles':pro,'search_query':searchQuery}
    return(render(request,'profiles.html',context))

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills=profile.skills_set.exclude(description="")
    OtherSkills=profile.skills_set.filter(description="")
    context={'profile':profile,'topSkills':topSkills,'OtherSkills':OtherSkills}
    return(render(request,'user-profile.html',context))

@login_required(login_url='loginUser')
def userAccount(request):
    profile=request.user.profile
    projects=profile.project_set.all()
    topSkills=profile.skills_set.all()
    context={'profile':profile,'topSkills':topSkills,'projects':projects}
    return(render(request,'account.html',context))

@login_required(login_url='loginUser')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return(redirect('userAccount'))
    context={'form':form}
    return(render(request,'profile_form.html',context))

@login_required(login_url='loginUser')
def createSkill(request):
    skills=SkillForm
    context={'skills':skills}
    profile=request.user.profile
    if request.method=='POST':
        skills=SkillForm(request.POST)
        if skills.is_valid():
            skill=skills.save(commit=False)
            skill.owner=profile
            skill.save()
            return(redirect('userAccount'))
    return(render(request,'skill_form.html',context))

def updateSkill(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)
    skills=SkillForm(instance=skill)
    context={'skills':skills}
    if request.method=='POST':
        skills=SkillForm(request.POST,instance=skill)
        if skills.is_valid():
            skill=skills.save(commit=False)
            skill.owner=profile
            skill.save()
            return(redirect('userAccount'))
    return(render(request,'updateSkill.html',context))


def deleteSkill(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        return(redirect('userAccount'))
    return(render(request,'deleteSkill.html'))