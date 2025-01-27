from .models import *
from django.db.models import Q

def searchProfiles(request):
    searchQuery=''
    if request.GET.get('search_query'):
        searchQuery=request.GET.get('search_query')
    skills=Skills.objects.filter(name__iexact=searchQuery)
    pro=Profile.objects.distinct().filter(Q(name__icontains=searchQuery) | Q(skills__in=skills))
    return(pro,searchQuery)