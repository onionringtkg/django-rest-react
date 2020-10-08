from rest_framework import serializers
from . import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerialiser):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwards = { 'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TaskSerializer(serializers.ModelSerialiser):

    #read_onlyにすると、post通信の際にカラムが不要になる？（要チェック）
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at')