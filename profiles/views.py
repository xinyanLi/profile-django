from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Profile, ProfileSerializer
    
def index(request):
    return render(request, 'index.html')

class ProfileMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileList(ProfileMixin, generics.ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    pass

class ProfileDetail(ProfileMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Return a specific task, update it, or delete it.
    """
    pass
