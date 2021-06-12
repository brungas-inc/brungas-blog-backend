from django.urls import path
from . import views,views2

# from  .views import order_views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
 
# )

urlpatterns =[
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.RegisterUserView.as_view(), name= 'register'),
    path('post/<int:postId>/like-count/', views2.GetPostLikestCountsViewSet.as_view(), name= 'count'),
    # path('post/<int:id>/delete/', views.PostDeleteAPI.as_view(), name= 'post-delete'),
    path('post/<int:pk>/add-like/', views2.AddLikeAPI.as_view(), name= 'add-like'),
    ]