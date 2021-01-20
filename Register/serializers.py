from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message={"email exist"})]
            )
            
    username = serializers.CharField(
            min_length=3
            )

    password = serializers.CharField(write_only=True,
            required=True,
            validators=[validate_password])

    passwordVerify = serializers.CharField(write_only=True, 
            required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'passwordVerify')


    def validate(self, attrs):
        if attrs['password'] != attrs['passwordVerify']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user