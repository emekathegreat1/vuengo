from django.shortcuts import render


from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




# To render data into frontend, and 
# handle requests from user, we need 
# to create a view. In Django REST Framework, 
# we call these as viewsets