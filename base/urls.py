from django.urls import path, include
from .views import authView, home, logout_view,login_view,change_username, change_password, profile

urlpatterns = [
 path("", login_view, name="login"),
 path("signup/", authView, name="authView"),
 path("home/", home, name="home"),  
 path("logout/", logout_view, name="logout"),
 path("accounts/", include("django.contrib.auth.urls")),
 path('profile/', profile, name='profile'),
 path('change-username/', change_username, name='change-username'),
 path('change-password/', change_password, name='change-password'),
]
