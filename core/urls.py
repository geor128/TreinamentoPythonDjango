from django.contrib import admin
from django.urls import path, include
from .views import home, contato
from simplemooc import settings
from django.conf.urls.static import static

app_name = "core"
urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),

]
              #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


