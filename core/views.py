from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    usuario = 'george silva macedo'
    return render(request,'home.html',{'usuario':usuario})

def contato(request):
    return render(request,'contato.html')