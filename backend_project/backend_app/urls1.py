from rest_framework import routers
from .views import PostViewSet,CommentViewSet, PostLikesViewSet
from .views2 import( GetCommentsByPostViewSet, GetPostByUserViewSet,
 GetPostLikesViewSet, GetPostLikesCountsViewSet)

router = routers.DefaultRouter()

router.register('all_posts',PostViewSet , 'all_posts')
router.register('all_comments',CommentViewSet , 'all_comments')
router.register('all_likes',PostLikesViewSet , 'all_likes')

# FITTERED URL
router.register(r'post/(?P<postId>\d+)/comments',GetCommentsByPostViewSet, 'post-coments')
router.register(r'post/user/(?P<userId>\d+)/posts',GetPostByUserViewSet, 'user-posts')
router.register(r'post/(?P<postId>\d+)/likes',GetPostLikesViewSet, 'posts-likes')
# router.register(r'post/(?P<postId>\d+)/likes-counts',GetPostLikestCountsViewSet, 'likes-count')
  
urlpatterns = router.urls  