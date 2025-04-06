# 🐍 Atividade Prática com Django - Modelos e Admin

## 🎯 Objetivo

Aprender a:

- Instalar e configurar um projeto Django
- Criar uma app
- Definir modelos com campos variados
- Aplicar migrações
- Registrar modelos no Django Admin

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes)

---

## 🚀 Etapas da Atividade

### ✅ 1. Criar um Ambiente Virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS ou
venv\Scripts\activate       # Windows
```

### ✅ 2. Instalar o Django

```bash
pip install django
```

### ✅ 3. Criar um Projeto Django

```bash
django-admin startproject myproject
cd myproject
```

### ✅ 4. Criar um App chamado `core`

```bash
python manage.py startapp core
```

Em `myproject/settings.py`, adicione `'core'` em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

### ✅ 5. Criar Três Modelos com Campos Diversos

Abra `core/models.py` e defina os seguintes modelos:

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    born_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
```

### ✅ 6. Criar e Aplicar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### ✅ 7. Criar Superusuário

```bash
python manage.py createsuperuser
```

### ✅ 8. Registrar os Modelos no Admin

Abra `core/admin.py`:

```python
from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Client)
```

### ✅ 9. Rodar o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) e entre com o superusuário.

---

## 📌 Entrega da Atividade

- O admin deve mostrar os 3 modelos cadastrados.
- Os campos devem estar funcionais para inserção de dados.

---

## 📚 Dica

Use a documentação oficial como apoio:
🔗 https://docs.djangoproject.com/pt-br/stable/topics/db/models/

---

🚀 **Bônus:** Se quiser avançar, tente adicionar filtros, buscas ou relacionamento entre modelos no Django Admin! 💻

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Boa prática e divirta-se! 🚀
