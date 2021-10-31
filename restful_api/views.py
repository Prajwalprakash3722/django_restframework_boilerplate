from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.


@api_view(['GET'])
def index(request):
    msg = {
        'message': 'API Landing Page'
    }
    return Response(msg)


@api_view(['GET'])
def task_detail(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def single_task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def single_task_modify(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def single_task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    msg = {
        'message': f'Task-{pk} Deleted'
    }
    return Response(msg)
