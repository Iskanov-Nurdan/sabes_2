from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView,DestroyAPIView


from .models import Task
from .serializers import *
# Create your views here.


class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPICreate (CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIRetrieve(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIDestroy(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
