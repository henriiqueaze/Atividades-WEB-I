from django import forms
from .models import Product, Client, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'available', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'born_date', 'is_active']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'born_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da categoria'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição (opcional)', 'rows': 3}),
        }
