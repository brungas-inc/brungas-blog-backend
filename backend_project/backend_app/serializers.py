from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer
import django.contrib.auth.password_validation as validators


from .models import Post, Comment, PostLikes


class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only =True)
    _id = serializers.SerializerMethodField(read_only =True)
    isAdmin = serializers.SerializerMethodField(read_only =True)


    class Meta:
        model = User
        fields =[ 'id','username','email', 'first_name','first_name','isAdmin' ]

   
    def get__id(self,obj):
        
        return obj.id 

    def get_isAdmin(self,obj): 
        
        return obj.is_staff 


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only =True)
    class Meta:
        model = User
        fields =[ 'token']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
        
        

class RegisterSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff= validated_data['is_staff'],
            email=validated_data['email']

        )
        return user

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only':True}}

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups']


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PostSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source="user.username",read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source="user.username",read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    likers=serializers.CharField(source="likeusers.username",read_only=True)
    class Meta:
        model = PostLikes
        fields = ['likeusers','likers']
