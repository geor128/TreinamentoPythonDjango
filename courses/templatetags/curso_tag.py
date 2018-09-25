from django.template import Library
# O library deve ser impotado para registrar suas tags
register = Library()

from courses.models import Inscricao

@register.inclusion_tag('courses/templatetags/meu_cursos.html')
def meu_curso(nome):
    inscricoes = Inscricao.objects.filter(nome=nome)

    context = {
        'inscricoes': inscricoes
    }

    return context
