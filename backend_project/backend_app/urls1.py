from rest_framework import routers
from .views import PostViewSet,CommentViewSet, PostLikesViewSet, UserProfileViewSet
from .views2 import( GetCommentsByPostViewSet, GetPostByUserViewSet,
 GetPostLikestViewSet, GetPostLikestCountsViewSet)

router = routers.DefaultRouter()

router.register('all_posts',PostViewSet , 'all_posts')
router.register('all_comments',CommentViewSet , 'all_comments')
router.register('all_likes',PostLikesViewSet , 'all_likes')


# FITTERED URL
router.register(r'post/(?P<postId>\d+)/comments',GetCommentsByPostViewSet, 'post-coments')
router.register(r'post/user/(?P<userId>\d+)/posts',GetPostByUserViewSet, 'user-posts')
router.register(r'post/(?P<postId>\d+)/likes',GetPostLikestViewSet, 'posts-likes')
# router.register(r'post/(?P<postId>\d+)/likes-counts',GetPostLikestCountsViewSet, 'likes-count')
  
urlpatterns = router.urls  