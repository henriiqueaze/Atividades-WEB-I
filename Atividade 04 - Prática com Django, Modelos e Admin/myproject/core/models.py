from django.db import models

class Category(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=8, decimal_places=2)
    available = models.BooleanField("Available", default=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.name

class Client(models.Model):
    full_name = models.CharField("Full Name", max_length=120)
    email = models.EmailField("Email", unique=True)
    born_date = models.DateField("Birth Date")
    is_active = models.BooleanField("Active", default=True)

    def __str__(self):
        return self.full_name
