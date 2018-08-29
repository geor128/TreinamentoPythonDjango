from django.shortcuts import render, get_object_or_404
from courses.models import Course
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