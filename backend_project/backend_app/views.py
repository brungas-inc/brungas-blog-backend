from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import Post, Comment,PostLikes 
from rest_framework import fields, generics, permissions, viewsets
from django.contrib.auth.models import User
from .serializers import (
    UserSerializerWithToken , RegisterSerializer,
    PostSerializer,CommentSerializer, PostLikestSerializer)

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


# VIEW SETS

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostSerializer

# class PostDeleteAPI(generics.UpdateAPIView):
#     queryset = Post.objects.filter(is_active=True)
#     lookup_url_kwarg='id'
#     serializer_class = PostSerializer
#     fields=['is_active']


   
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_active=True)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class =CommentSerializer

   
class PostLikesViewSet(viewsets.ModelViewSet):
    queryset = PostLikes.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostLikestSerializer