from django.urls import path

from . import views
from Login import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('hellow', views.LoginView.as_view(), name='Login'),

]