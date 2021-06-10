from django.urls import path
from . import views
# from  .views import order_views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
 
# )

urlpatterns =[
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]