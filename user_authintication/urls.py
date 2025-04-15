from django.urls import path
from . import views
urlpatterns = [
    path('login', views.LoginPage, name='login'),
    path('register', views.RegisterPage, name='register'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.ProfilePage, name='profile'),

    path("recent/",views.details),
    path('successfully/',views.send)
]