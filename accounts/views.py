from accounts.forms import RegistroForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from simplemooc import settings
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
# Create your views here.

'''def CriarUsuarios(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password'])
            user.save()
            return redirect('/conta/entrar/')

    else:
        form = RegistroForm(initial={'is_staff':True})
    return render(request, template_name,{'form':form})'''

def CriarUsuarios(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')

    else:
        form = RegistroForm()
    return render(request, template_name,{'form':form})

def Sair(request):
    logout(request)
    return redirect(settings.LOGOUT_URL)

def Dashboard(request):
    template_name = 'accounts/dashboard.html'

    return render(request, template_name,{'nome':'Jobileia'})

def Edit(request):
    template_name = 'accounts/edit.html'
    usuario = User.objects.get(username=request.user)
    return render(request, template_name,{'nome':'Jobileia'})

def EditPassword(request):
    template_name = 'accounts/edit_password.html'

    return render(request, template_name,{'nome':'Jobileia'})