from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from users.models import Profile
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):
    print('user:',request.user)
    profileInfo=Profile.objects.all()
    serializers=ProfileSerializer(profileInfo,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def addData(request):
    serializer=ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return(Response(serializer.data))

@api_view(['GET'])
def getProfile(request,pk):
    profileInfo=Profile.objects.get(id=pk)
    serializers=ProfileSerializer(profileInfo,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getProject(request,pk):
    projectInfo=Project.objects.get(id=pk)
    serializers=ProjectSerializer(projectInfo,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getProjects(request):
    print('USER:',request.user)
    projectInfo=Project.objects.all()
    serializers=ProjectSerializer(projectInfo,many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProjectVote(request,pk):
    project=Project.objects.get(id=pk)
    user=request.user.profile
    data=request.data
    review,created = Review.objects.get_or_create(owner=user,project=project)
    review.value=data['value']
    review.save()
    print("data:",request.data)
    serializers=ProjectSerializer(project,many=False)
    return Response(serializers.data)