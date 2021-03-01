"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api.view import views
from api.view import business_view
from api.view import user_view

urlpatterns = [
    path('admin/login/', views.LoginView.as_view(),name="Login"),
    path('admin/getUserInfo/', views.GetUserInfo.as_view(),name="getUserInfo"),
    path('admin/getRouter/',views.GetRouter.as_view(),name="getRouter"),
    path('admin/getPowerTree/',views.GetPowerTree.as_view(),name="admin/getPowerTree/"),

    path('user/login/',user_view.UserLogin.as_view(),name="user/login/"),
    path('user/getUserInfo/',user_view.GetUserInfo.as_view(),name="user/getUserInfo/"),
    path('user/',user_view.UserView.as_view(),name="user"),
    path('putuser/',user_view.PutUserView.as_view(),name=""),
    path('picture/',user_view.Picture.as_view(),name="picture"),

    path('admin/',views.Admin.as_view(),name="admin"),
    path('admin/resetRole/',views.ResetRole.as_view(),name="admin/resetRole"),
    path('admin/resetPassword/',views.ResetPassword.as_view(),name="admin/resetPassword"),

    path('roles/',views.Roles.as_view(),name="roles"),
    path('postCate/',business_view.PostCate.as_view(),name="Invitation"),
    path('systemMessage/',business_view.SystemMessage.as_view(),name="systemMessage"),
    path('ad/',business_view.Ad.as_view(),name="ad"),
    path('ad/updateStatus/',business_view.UpdateStatus.as_view(),name="ad/updateStatus"),
    path('permission/',views.Permission.as_view(),name="permission"),
    path('admin/addmodels/', views.AddModels.as_view()),
]
