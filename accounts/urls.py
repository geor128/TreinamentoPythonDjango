from accounts.views import CriarUsuarios
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import index
app_name = "accounts"

urlpatterns = [
    #path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    #path('profile/', index, name='profile'),
    path('cadastrar/', CriarUsuarios, name='cadastrar'),
]

