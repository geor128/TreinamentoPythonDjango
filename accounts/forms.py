from django.contrib.auth.models import User
#from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

'''class RegistroForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username','email','password','is_staff']
         widgets = {
             'is_staff': forms.HiddenInput()

         }'''

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    '''def clean_email(self):
        email=self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Já existe usuário com esse email')
        return email'''

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com esse email')
        else:
            return email
