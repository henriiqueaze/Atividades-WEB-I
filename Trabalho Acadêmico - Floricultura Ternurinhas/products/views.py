# views.py
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm, ProductFilterForm


def product_list(request):
    form = ProductFilterForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        if name:
            products = products.filter(name__icontains=name)

        tipo = form.cleaned_data.get('type')
        if tipo:
            products = products.filter(tipo=tipo)

        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        if min_price is not None:
            products = products.filter(preco__gte=min_price)
        if max_price is not None:
            products = products.filter(preco__lte=max_price)

        sort = form.cleaned_data.get('sort')
        if sort == 'name':
            products = products.order_by('name')
        elif sort == 'price':
            products = products.order_by('preco')

    return render(request, 'products/product_list.html', {'form': form, 'products': products})


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully created!"


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"


class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"
