from django.urls import path
from .views import lista_filmes, cadastrar_filme, deletar_filme

urlpatterns = [
    path('', lista_filmes, name='lista_filmes'),
    path('cadastrar/', cadastrar_filme, name='cadastrar_filme'),
    path('deletar/<int:filme_id>/', deletar_filme, name='deletar_filme'),
]
