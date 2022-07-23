# forms.py
from django import forms
from .models import *
  
class MuseumForm(forms.ModelForm):
    class Meta:
        model = Museum
        fields = ['img_name', 'img']
        
class CurrentFrameForm(forms.ModelForm):
    class Meta:
        model = CurrentFrame
        fields = ['img_name', 'img']