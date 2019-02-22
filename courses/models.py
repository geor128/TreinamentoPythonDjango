from django.db import models
from simplemooc import settings
# Create your models here.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query))

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date  = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField(
        'Criado em ', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em ', auto_now=True
    )
    object = CourseManager()

    def __str__(self):
        return self.name

    #@models.permalink
    def get_absolute_url(self):
        #from django.urls import reverse
       # return ('cursos:detalhes/',{'slug_id':self.slug})
        return self.slug

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class Inscricao(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )
    nome = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Nome do usuário', related_name='inscricao', on_delete=True )
    curso = models.ForeignKey(Course, verbose_name='Curso', related_name='inscricao', on_delete=True)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    created_at = models.DateTimeField(
        'Criado em ', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em ', auto_now=True
    )
    def active(self):
        self.status = 1
        self.save()
    def is_aprovado(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('nome','curso'),)

class Announcement(models.Model):
    course = models.ForeignKey(Course, verbose_name='Curso', on_delete=True, related_name='announcement')
    title = models.CharField('Titulo', max_length=100)
    content = models.TextField('Conteudo')
    created_at = models.DateTimeField(
        'Criado em ', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em ', auto_now=True
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'
        ordering = ['-created_at']

class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, verbose_name='Anúncio', related_name='comments', on_delete=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário', on_delete=True)
    comment = models.TextField('Comentário')
    created_at = models.DateTimeField(
        'Criado em ', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em ', auto_now=True
    )
    class Meta:
       verbose_name = 'Comentário'
       verbose_name_plural = 'Comentários'
       ordering = ['created_at']