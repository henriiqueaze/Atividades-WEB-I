from django.shortcuts import render, redirect
from .forms import ProductForm, ClientForm, CategoryForm
from django.http import HttpResponse

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_success')
    else:
        form = ProductForm()
    return render(request, 'core/create_product.html', {'form': form})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_success')
    else:
        form = ClientForm()
    return render(request, 'core/create_client.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_success')
    else:
        form = CategoryForm()
    return render(request, 'core/create_category.html', {'form': form})

def product_success(request):
    return HttpResponse("Produto cadastrado com sucesso!")

def client_success(request):
    return HttpResponse("Cliente cadastrado com sucesso!")

def category_success(request):
    return HttpResponse("Categoria cadastrada com sucesso!")
