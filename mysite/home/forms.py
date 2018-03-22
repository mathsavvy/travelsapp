from django import forms
from django.db import model
from django.forms import widgets
from .models import Post


class CabRideForm(forms.ModelForm):
    class Meta:
        model = CabRide
        fields = ['pickup', 'drop', 'time', 'jourtype']
        widgets = {'gender': forms.RadioInput}