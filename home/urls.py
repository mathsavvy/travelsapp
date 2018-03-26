from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='befsignin'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup, name='signup'),
    path('auth/',views.auth, name='auth'),
    path('register/',views.register, name='register'),
    path('retrieve/',views.retrieve, name='retrieve'),
    path('forgotpassword/',views.forgpass, name='forgpass'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('cab/', views.cab, name='cab'),
    path('confirmation/', views.cab_book, name='cab_book'),
]
