from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='befsignin'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup, name='signup'),
    path('auth/',views.auth, name='auth'),
    path('register/',views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('cab/', views.cab, name='cab'),
    path('cab_book/', views.cab_book, name='cab_book')
]
