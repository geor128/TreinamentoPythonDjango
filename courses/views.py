from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Inscricao
# Create your views here.
def index(request):
    cursos = Course.object.all()
    template_name = 'courses/index.html'
    return render(request, template_name,{'cursos':cursos})

#def detalhes(request, id_curso):
 #   curso = get_object_or_404(Course, pk=id_curso)
  #  template_name = 'courses/detalhes_curso.html'

   # return render(request, template_name,{'curso':curso})

def detalhes(request, slug_curso):
    "Esta parte exibe detalhes do curso escolhido"
    from courses.forms import ContatoForm
    curso = get_object_or_404(Course, slug=slug_curso)
    template_name = 'courses/detalhes_curso.html'
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.send_mail(curso.name)
            return render(request, template_name,{'curso':curso,'form':form})

    else:
        form = ContatoForm()
    return render(request, template_name,{'curso':curso,'form':form})

'''@login_required
def matricular_curso(request, curso):
    curso = get_object_or_404(Course, pk=curso)
    inscricao = Inscricao.objects.create(status=0,nome=request.user, curso=curso )
    inscricao.save()
    return redirect('accounts:dashboard')'''

@login_required
def matricular_curso(request, slug_curso):
    curso = get_object_or_404(Course, slug=slug_curso)
    inscricao, create = Inscricao.objects.get_or_create(nome=request.user, curso=curso )
    if create:
        inscricao.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')
    return redirect('accounts:dashboard')
