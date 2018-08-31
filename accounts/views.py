from accounts.forms import RegistroForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
# Create your views here.

def CriarUsuarios(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/conta/entrar/')

    else:
        form = RegistroForm(initial={'is_staff':True})
    return render(request, template_name,{'form':form})