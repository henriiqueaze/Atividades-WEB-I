from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'price']
    list_filter = ['category', 'available']

class ClientAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'email']
    list_filter = ['is_active']

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Client, ClientAdmin)
