# 📚 Django MVT - Projeto de Exemplo: Biblioteca de Livros

Este projeto é um exemplo simples para demonstrar o uso de:

- Django com PostgreSQL
- Views baseadas em função
- Templates com dados dinâmicos
- Upload e exibição de imagens (mídia)
- Organização de templates, estáticos e media

---

## 🚀 Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure seu banco PostgreSQL no `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'biblioteca',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Execute migrações

```bash
python manage.py migrate
```

### 4. Carregue os dados no projeto

```bash
python manage.py loaddata fixtures/fixture_biblioteca.json
```

### 5. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

### 6. Acesse a aplicação

Visite [http://localhost:8000](http://localhost:8000) para ver a lista de livros.

Você pode adicionar livros manualmente pelo admin ou adicionando views de criação.

---

## 📝 Atividade: Catálogo de Filmes

Agora é a sua vez!

🎯 **Objetivo**: Criar um projeto Django semelhante ao exemplo da Biblioteca, mas com o tema **Catálogo de Filmes**.

### 📌 Requisitos:

1. Criar um novo projeto Django com um app chamado `core`
2. Criar o modelo `Filme` com os seguintes campos:
   - `titulo` (CharField)
   - `descricao` (TextField)
   - `ano_lancamento` (IntegerField)
   - `imagem` (ImageField - upload para `filmes/`)
3. Criar uma view baseada em função chamada `lista_filmes`
4. Criar um template para listar os filmes com suas informações
5. Exibir as imagens no template
6. Aplicar um CSS básico via arquivos estáticos
7. Organizar os templates e estáticos como no exemplo
8. Utilizar o `admin` ou `shell` para cadastrar pelo menos 5 filmes com imagem

### 🧪 Extras (opcional):

- Criar um template base com herança
- Criar uma página de detalhe do filme
- Estilizar com Bootstrap ou Tailwind

### 📁 Estrutura esperada:

```
catalogo_filmes/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── filmes/
│   │       └── lista.html
│   ├── static/
│   │   └── filmes/
│   │       └── css/estilo.css
├── media/
│   └── filmes/
│       └── imagem1.jpg ...
```

### 📤 Entrega

- Subir no GitHub ou enviar ZIP com:
  - Código fonte do projeto
  - Imagens usadas (em `media/`)
  - Prints do funcionamento (opcional)

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Bons estudos e divirta-se criando seu próprio catálogo! 🍿