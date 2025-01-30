from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Profile
from .serializers import ProfileSerializer

@api_view(['GET'])
def getData(request):
    profileInfo=Profile.objects.all()
    serializers=ProfileSerializer(profileInfo,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def addData(request):
    serializer=ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return(Response(serializer.data))