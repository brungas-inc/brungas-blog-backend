from django.db.models.aggregates import Count
from rest_framework import permissions, viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from .models import Post, Comment, PostLikes


from .serializers import (
        PostSerializer,CommentSerializer, PostLikestSerializer)


class GetPostByUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated ]

    def get_queryset(self):
        user_id = self.kwargs.get('userId')
        return Post.objects.filter(user=user_id)

class GetCommentsByPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return Comment.objects.filter(post=post_id)

class GetPostLikestViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PostLikestSerializer
   

    def get_queryset(self):
        post_id = self.kwargs.get('postId')
        return PostLikes.objects.filter(likepost=post_id)


class GetPostLikestCountsViewSet(APIView):
  
    def get(self,request,postId):
        # serializer = PostLikestSerializer()
        like_count= PostLikes.objects.filter(likepost=postId).count()
        content= {'likes_count': like_count}
        return Response(content)

class AddLikeAPI(APIView):
    serializer_class=PostLikestSerializer
    def post(self,request,pk):
        likeusers = request.user
        likepost = Post.objects.get(id=pk)
        if PostLikes.objects.filter(likepost=likepost).filter(likeusers=likeusers).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            PostLikes.objects.create(likepost=likepost,likeusers=likeusers)
            return Response(status=status.HTTP_201_CREATED)

