from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    
    path('post_thread', views.post_thread),
    path('get_thread', views.get_threads),
]