from django.conf.urls import url

from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.index,name='befsignin'),
    url('signin/', views.signin,name='signin'),
    url('signup/', views.signup, name='signup'),
    url('auth/',views.auth, name='auth'),
    url('about',views.about, name='about'),
    url('aboutus/', views.aboutus, name='aboutus'),
    url('contact/', views.contact, name='contact'),
    url('contactus/',views.contactus, name='contactus'),
    url('register/',views.register, name='register'),
    url('retrieve/',views.retrieve, name='retrieve'),
    url('forgotpassword/',views.forgpass, name='forgpass'),
    url('home/', views.home, name='home'),
    url('logout/', views.logout_view, name='logout'),
    url('cab/', views.cab, name='cab'),
    url('confirmation/', views.cab_book, name='cab_book'),
]

