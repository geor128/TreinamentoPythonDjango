from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from simplemooc import settings
import re


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome de usuário', max_length=30, unique=True, null=True, blank=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome de usuário só pode conter letras, digitos'
                                                                      'ou os seguintes caracteres:@/./+/-/_','invalid')])
    email = models.CharField('Email do usuário',max_length=40, unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('Membro da equipe', blank=True, default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username or self.name

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class RedefinirSenha(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Nome do usuário', related_name='resets', on_delete=True )
    key = models.CharField('Chave', max_length = 100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado ?', default=False, blank=True)

    def __str__(self):
        return '{0}em{1}'.format(self.nome, self.created_at)

    class Meta:
        verbose_name = 'Redefinir senha'
        verbose_name_plural = 'Redefinir senhas'
        ordering = ['-created_at']