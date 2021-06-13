from django.urls import path
from . import views,views2


urlpatterns =[
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('users/register/', views.RegisterUserView.as_view(), name= 'register'),
    path('post/<int:postId>/like-count/', views2.GetPostLikesCountsViewSet.as_view(), name= 'count'),
    # path('post/<int:id>/delete/', views.PostDeleteAPI.as_view(), name= 'post-delete'),
    path('post/<int:pk>/add-like/', views2.AddLikeAPI.as_view(), name= 'add-like'),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('post/single-post/<int:id>/',views.GetSinglePostsAPI.as_view(),name='sing-lepost'),

    ]