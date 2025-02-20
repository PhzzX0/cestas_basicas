from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('instituicoes/', views.lista_instituicoes, name='lista_instituicoes'),
    path('instituicoes/criar/', views.criar_instituicao, name='criar_instituicao'),
    path('doadores/', views.lista_doadores, name='lista_doadores'),
    path('doadores/criar/', views.criar_doador, name='criar_doador'),
    path('cestas/', views.lista_cestas, name='lista_cestas'),
    path('cestas/criar/', views.criar_cesta, name='criar_cesta'),
]