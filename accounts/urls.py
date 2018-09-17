from accounts.views import CriarUsuarios, Sair, Edit, EditPassword, ResetarPassword, ResetarPasswordConfirmar
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
    path('edit/', Edit, name='edit'),
    path('edit_passsword/', EditPassword, name='edit_password'),
    path('redefinir_senha/', ResetarPassword, name='redefinir_senha'),
    path('redefinir_senha_confirmar/<str:key>/', ResetarPasswordConfirmar, name='redefinir_senha_confirmar'),

]

