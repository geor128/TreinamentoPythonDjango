# Generated by Django 2.1 on 2018-09-16 18:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180910_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedefinirSenha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(blank=True, default=False, verbose_name='Confirmado ?')),
            ],
            options={
                'verbose_name': 'Redefinir senha',
                'verbose_name_plural': 'Redefinir senhas',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O nome de usuário só pode conter letras, digitosou os seguintes caracteres:@/./+/-/_', 'invalid')], verbose_name='Nome de usuário'),
        ),
        migrations.AddField(
            model_name='redefinirsenha',
            name='nome',
            field=models.ForeignKey(on_delete=True, related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Nome do usuário'),
        ),
    ]
