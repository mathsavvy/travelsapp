from django import forms
from django.db import model
from django.forms import widgets
from .models import Post

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class Userextradata(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ['regno', 'mob_no']

class CabRideForm(forms.ModelForm):
    class Meta:
        model = CabRide
        fields = ['pickup', 'drop', 'time', 'jourtype']
        widgets = {'gender': forms.RadioInput}