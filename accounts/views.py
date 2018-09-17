from accounts.forms import RegistroForm, EditForm, RedefinirSenhaForm
from accounts.models import RedefinirSenha
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from simplemooc import settings
from core.utils import generate_hash_key
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
# Create your views here.
User = get_user_model()

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

def ResetarPassword(request):
    template_name = 'accounts/redefinirsenha.html'
    context = {}
    form = RedefinirSenhaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, template_name, context)
def ResetarPasswordConfirmar(request, key):
    template_name = 'accounts/redefinir_senha_confirmar.html'
    context = {}
    reset = get_object_or_404(RedefinirSenha, key=key)
    form = SetPasswordForm(user=reset.nome, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form']= form
    return render(request, template_name, context)
def Sair(request):
    logout(request)
    return redirect(settings.LOGOUT_URL)
@login_required
def Dashboard(request):
    template_name = 'accounts/dashboard.html'

    return render(request, template_name,{'nome':'Jobileia'})
@login_required()
def Edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditForm(instance=request.user)
            context['success'] = True
    else:
        #form = EditForm(initial={'username':user.username,'email':user.email,'first_name':user.first_name,'last_name':user.last_name})
        form = EditForm(instance=request.user)
    context['form'] = form
    return render(request, template_name,context)

'''def EditPassword(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = FormEditPassword(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            form = FormEditPassword()
            context['success'] = True
    else:
        #form = EditForm(initial={'username':user.username,'email':user.email,'first_name':user.first_name,'last_name':user.last_name})
        form = FormEditPassword()
    context['form'] = form
    return render(request, template_name, context)'''
@login_required()
def EditPassword(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)