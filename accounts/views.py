from accounts.forms import RegistroForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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