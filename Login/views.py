from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class LoginView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#
