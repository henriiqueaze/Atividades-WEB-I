from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm

# Create your views here.

def lista_filmes(request):
    filmes = Filme.objects.all().order_by('-ano_lancamento')
    return render(request, 'filmes/lista.html', {'filmes': filmes})

def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/cadastro.html', {'form': form})

def deletar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return redirect('lista_filmes')
