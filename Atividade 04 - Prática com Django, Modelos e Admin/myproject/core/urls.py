from django.urls import path
from . import views

urlpatterns = [
    path('produto/novo/', views.create_product, name='create_product'),
    path('cliente/novo/', views.create_client, name='create_client'),
    path('produto/sucesso/', views.product_success, name='product_success'),
    path('cliente/sucesso/', views.client_success, name='client_success'),
    path('categoria/novo/', views.create_category, name='create_category'),
    path('categoria/sucesso/', views.category_success, name='category_success'),
]
