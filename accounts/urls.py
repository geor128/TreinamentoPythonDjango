from accounts.views import CriarUsuarios, Sair
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import Dashboard
app_name = "accounts"

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    #path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    #path('profile/', index, name='profile'),
    path('cadastrar/', CriarUsuarios, name='cadastrar'),
    path('sair/', Sair, name='sair'),

]

