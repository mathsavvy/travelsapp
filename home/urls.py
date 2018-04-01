from django.conf.urls import url

from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^', views.index,name='befsignin'),
    url(r'^signin/', views.signin,name='signin'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^auth/',views.auth, name='auth'),
    url(r'^about',views.about, name='about'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^contactus/',views.contactus, name='contactus'),
    url(r'^register/',views.register, name='register'),
    url(r'^retrieve/',views.retrieve, name='retrieve'),
    url(r'^forgotpassword/',views.forgpass, name='forgpass'),
    url(r'^home/', views.home, name='home'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^cab/', views.cab, name='cab'),
    url(r'^confirmation/', views.cab_book, name='cab_book'),
]

