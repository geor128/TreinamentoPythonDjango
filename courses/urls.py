from django.urls import path, include
from courses.views import index, detalhes

app_name = "courses"
urlpatterns = [
    path('', index, name='index'),
    #path('detalhes/<int:id_curso>', detalhes, name='detalhes'),
    path('detalhes/<slug:slug_curso>', detalhes, name='detalhes'),

]

