from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import UserSerializerWithToken ,UserSerializer, RegisterSerializer

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer