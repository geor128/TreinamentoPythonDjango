from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from courses.forms import CommentForm
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

@login_required#enrollment
def matricular_curso(request, slug_curso):
    curso = get_object_or_404(Course, slug=slug_curso)
    inscricao, create = Inscricao.objects.get_or_create(nome=request.user, curso=curso )#Enrrolment
    if create:
        inscricao.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')
    return redirect('accounts:dashboard')

@login_required()
def desmatricular_curso(request, slug_curso): #desfazer inscrição
    curso = get_object_or_404(Course, slug=slug_curso)
    inscricao = get_object_or_404(Inscricao, nome=request.user,curso=curso)
    if request.method == 'POST':
        inscricao.delete()
        messages.success(request, 'Sua inscrição foi cancelada com sucesso!!!!!')
        return redirect('accounts:dashboard')
    template = 'courses/undo_enrollment.html'
    context = {
        'inscricao':inscricao,
        'curso':curso,
    }
    return render(request, template, context)

@login_required
def announcements(request, slug_curso):
    curso = get_object_or_404(Course, slug=slug_curso)
    if not request.user.is_staff:
        inscricao = get_object_or_404(Inscricao, nome=request.user, curso=curso)
        if not inscricao.is_aprovado():
            messages.error(request, 'A sua inscrição está pendente')
            return redirect('accounts:dashboard')
    template = 'courses/announcements.html'
    context = {
        'curso': curso,
        'announcements': curso.announcement.all()#todos os anúncios do curso estão nessa variável
    }
    return render(request, template, context)

@login_required
def show_announcements(request, slug_curso, pk):
    curso = get_object_or_404(Course, slug=slug_curso)
    if not request.user.is_staff:
        inscricao = get_object_or_404(Inscricao, nome=request.user, curso=curso)
        if not inscricao.is_aprovado():
            messages.error(request, 'A sua inscrição está pendente')
            return redirect('accounts:dashboard')
    announcement = get_object_or_404(curso.announcement.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.announcement = announcement
        comment.user = request.user
        comment.save()
        form = CommentForm()
        messages.success(request, 'Seu comentário foi enviado com sucesso!!!')
    template = 'courses/show_announcement.html'

    context = {
        'curso': curso,
        'announcements': announcement,
        'form': form
    }
    return render(request, template, context)

