from django.contrib import admin
from django.urls import path
from .import views
from .views import CustomLoginView ,Registerpage
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('Login/', CustomLoginView.as_view(), name ='Login'),
    path('Logout/',LogoutView.as_view(next_page='Login'),name='logout'),
    path('register/', Registerpage.as_view(), name='register'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]