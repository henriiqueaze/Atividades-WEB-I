from django.urls import path
from . import views

urlpatterns = [
    path('product/new/', views.create_product, name='create_product'),
    path('client/new/', views.create_client, name='create_client'),
    path('product/success/', views.product_success, name='product_success'),
    path('client/success/', views.client_success, name='client_success'),
    path('category/new/', views.create_category, name='create_category'),
    path('category/success/', views.category_success, name='category_success'),
]
