from django.contrib.auth.models import User
#from django.forms import ModelForm
from django import forms

class RegistroForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username','email','password','is_staff']
         widgets = {
             'is_staff': forms.HiddenInput()

         }
