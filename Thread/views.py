from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User, Group
from Login.models import Thread,Communities
from rest_framework import viewsets
from Login.serializers import UserSerializer, ThreadSerializer, CommunitiesSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser 
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view

class ThreadViewSet(viewsets.ModelViewSet):
    q = 1
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def post_thread(request):
    currentid = request.user.id
    request.data["u_id"] = currentid
    serializer = ThreadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
def get_threads(request):
    threads = Thread.objects.all()
    serializer = ThreadSerializer(threads, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_thread(request, pk):
    try:
        thread = Thread.objects.get(pk=pk, u_id=request.user.id)
    except Thread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    thread.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    