from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    # Todos os dados
    path('array/', views.getArrayFull),

    # Criar um texto de teste
    path('array/createTeste', views.createTeste),

    # Upload imagem
    path('array/createImage', views.uploadImage),

    # Apagar tudo
    path('array/deleteall', views.deleteAll),

    # Dado do ID
    path('array/<str:pid>', views.getArrayId),



]
