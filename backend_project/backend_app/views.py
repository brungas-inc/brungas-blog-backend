from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment,PostLikes
from rest_framework import fields, generics, permissions, viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView


from .serializers import (
    UserProfileSerializer, UserSerializerWithToken ,
    RegisterSerializer,ChangePasswordSerializer,UserSerializer,
    PostSerializer,CommentSerializer, PostLikeSerializer)

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



class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class LogoutView(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         if request.is_authenticated():
#             request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class GetSinglePostsAPI(APIView):
    def get(self, request,id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=id)
        like_count= PostLikes.objects.filter(likepost=id).count()
        likers=PostLikes.objects.filter(likepost=id)
        post_serializer = PostSerializer(post)
        comments_serializer = CommentSerializer(comments, many=True)
        likers_serializer=PostLikeSerializer(likers,many=True)
        return Response({
            'post': post_serializer.data,
            'comments': comments_serializer.data,
            'likers':likers_serializer.data,
            'likes':like_count,
        })

# VIEW SETS





class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    authentication_classes = [IsAuthenticated, ]
    permission_classes= [IsAuthenticated,]
    def get(self, request):
        #deleting the token in order to logout
        request.user.auth_token.delete()
        return Response("Successfully Logged Out!", status= status.HTTP_200)


class UserProfileViewSet(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects
    serializer_class = UserProfileSerializer
    def get_object(self):
        obj = get_object_or_404(self.queryset, id=self.request.user.id)
        return obj

     

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = PostSerializer

# class PostDeleteAPI(generics.UpdateAPIView):
#     queryset = Post.objects.filter(is_active=True)
#     lookup_url_kwarg='id'
#     serializer_class = PostSerializer
#     fields=['is_active']


   
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_active=True)
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class =CommentSerializer

   
class PostLikesViewSet(viewsets.ModelViewSet):
    queryset = PostLikes.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = PostLikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = UserSerializer