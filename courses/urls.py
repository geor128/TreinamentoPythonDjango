from django.urls import path, include
from courses.views import index, detalhes, matricular_curso, announcements, desmatricular_curso, show_announcements

app_name = "courses"
urlpatterns = [
    path('', index, name='index'),
    #path('detalhes/<int:id_curso>', detalhes, name='detalhes'),
    path('detalhes/<slug:slug_curso>', detalhes, name='detalhes'),
    #path('inscricao/<str:curso>', matricular_curso, name='matricular_curso'),
    path('inscricao/<slug:slug_curso>', matricular_curso, name='matricular_curso'),
    path('cancelar-inscricao/<slug:slug_curso>', desmatricular_curso, name='desmatricular_curso'),
    path('announcements/<slug:slug_curso>', announcements, name='announcements'),
    path('show_announcements/<slug:slug_curso>/<slug:pk>', show_announcements, name='show_announcements'),


]

