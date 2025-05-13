# forms.py

from django import forms
from .models import Product  # ou Produto, use o nome real do seu model


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'tipo',
            'preco',
            'quantidade',
            'descricao',
            'foto',
        ]
        labels = {
            'name': 'Nome',
            'tipo': 'Tipo',
            'preco': 'Preço',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição',
            'foto': 'Foto',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Search by name')
    type = forms.ChoiceField(choices=[('', 'All')] + Product.TIPO_CHOICES, required=False, label='Filter by type')
    min_price = forms.DecimalField(required=False, decimal_places=2, max_digits=8, label='Min Price')
    max_price = forms.DecimalField(required=False, decimal_places=2, max_digits=8, label='Max Price')
    sort = forms.ChoiceField(choices=[('name', 'Name (A-Z)'), ('price', 'Price')], required=False, label='Sort by')
