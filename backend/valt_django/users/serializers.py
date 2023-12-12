# serializers.py
from rest_framework import serializers
from .models import (
    Usuario
)
from rest_framework.authtoken.models import Token



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
       

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
   
