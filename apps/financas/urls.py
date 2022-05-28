from django.urls import path

app_name = 'financas'

from . import views

urlpatterns = [
    path('nova_categoria/', views.nova_categoria, name='nova_categoria'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('', views.principal, name='principal')
]