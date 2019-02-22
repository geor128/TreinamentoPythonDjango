from courses.mail import send_mail_template
from courses.models import Inscricao
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from courses.models import Comment

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome:', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Messagem/Duvida',widget=forms.Textarea)

    def send_mail(self, curso):
        subject = ' [%s] Contato' % curso
        #mensagem = 'Nome: %(nome)s;E-mail: %(email)s;%(message)s'
        context = {
            'nome' : self.cleaned_data['nome'],
            'email' : self.cleaned_data['email'],
            'message' : self.cleaned_data['message'],
        }
       # message = mensagem % context
        template_name = 'courses/contato_email.html'
        send_mail_template(
            subject,template_name ,context, [settings.CONTACT_EMAIL]
        )
'''class InscriçãoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = '''

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']