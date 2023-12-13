from django.urls import path

from UserLogin.view import user_view

urlpatterns = [
    path('admin/login/', user_view.UserLogin.as_view(),name="Login"),
    path('admin/userinfo/', user_view.User.as_view(),name="userinfo"),
    path('admin/register/', user_view.Register.as_view(),name="register"),
]