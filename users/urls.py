from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from . import views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('add/user/',views.AddUser.as_view(),name="add_user"),
    path('users/',views.GetAllUsers.as_view(),name="all_users"),
    # path('update/user<string:username>',views.UpdateUser,name="update_user"),
    

    

]