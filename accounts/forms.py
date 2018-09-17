from accounts.models import RedefinirSenha
from core.utils import generate_hash_key
from core.mail import send_mail_template
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()#Sempre chama para que não use o 'User' do django
class RedefinirSenhaForm(forms.Form):
    email = forms.EmailField(label='Email')

    def clean_emal(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Não existe nenhum usuário com esse email')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        redefinir = RedefinirSenha(key=key, nome=user)
        redefinir.save()
        template_name = 'accounts/redefinir_senha_email.html'
        context = {
            'redefinir':redefinir#o que será passado como parametro
        }
        subject = 'Criar nova senha no simplemooc'
        send_mail_template(subject, template_name,context, [user.email])
'''class RegistroForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username','email','password','is_staff']
         widgets = {
             'is_staff': forms.HiddenInput()

         }'''


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação de senha está incorreta')
        return password2
    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

    '''def clean_email(self):
        email=self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Já existe usuário com esse email')
        return email'''

    '''def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com esse email')
        else:
            return email'''


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name']

    '''def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com esse email')
        return email'''

'''class FormEditPassword(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)#maneira 1 de aparecer asterisco
    class Meta:
        model = User
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(),#maneira 2 de aparecer asteriscos
        }'''


