from django.contrib.auth.models import User, Group
from Login.models import Thread,Communities
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    u_id = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            many=False)
    class Meta:
        model = Thread
        fields = ['Title','body','Post_time','SoftDelete','u_id']
class CommunitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Communities
        fields = ['Community_Name']#,'CreateDate'
    
    