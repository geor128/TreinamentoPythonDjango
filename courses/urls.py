from django.urls import path, include
from courses.views import index, detalhes, matricular_curso

app_name = "courses"
urlpatterns = [
    path('', index, name='index'),
    #path('detalhes/<int:id_curso>', detalhes, name='detalhes'),
    path('detalhes/<slug:slug_curso>', detalhes, name='detalhes'),
    #path('inscricao/<str:curso>', matricular_curso, name='matricular_curso'),
    path('inscricao/<slug:slug_curso>', matricular_curso, name='matricular_curso'),

]

