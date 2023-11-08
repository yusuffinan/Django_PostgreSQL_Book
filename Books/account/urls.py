from django.urls import path
from . import views

urlpatterns = [
    path('login_', views.user_login, name="login_"),
    path('register_', views.user_register, name="register_"),
    path('logout_', views.user_logout, name="logout_"),
    path('profile_', views.user_profile, name="profile_")


]
