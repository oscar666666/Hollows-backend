from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
class LoginView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def post_thread(request):
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#



@api_view(["POST"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def creat_communities(request):
    serializer = CommunitiesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)