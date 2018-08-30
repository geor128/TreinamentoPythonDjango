from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistroForm(ModelForm):
     class Meta:
         model = User
         fields = '__all__'