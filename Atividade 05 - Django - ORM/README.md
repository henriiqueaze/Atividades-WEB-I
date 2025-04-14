# 📘 Atividade Prática: Django ORM no Shell

## 🎯 Objetivo

Praticar o uso do **Django ORM** via **shell interativo**, entendendo como manipular e consultar dados diretamente pelo terminal.

---

## 🚀 Etapas da Atividade

### ✅ 1. Carregar os dados de exemplo

No terminal, dentro da pasta do projeto, execute:

```bash
python manage.py loaddata core/fixtures/dados.json
```

### ✅ 2. Acessar o shell

```bash
python manage.py shell
```

Ou, se tiver `django-extensions`:

```bash
python manage.py shell_plus
```

---

## 🧪 Desafios com ORM

### 🔹 1. Listar todos os clientes cadastrados

```python
# saída esperada: Alice Souza
```

![Resolução - Desafio 1](assets/images/Desafio%201.png)

### 🔹 2. Criar um novo cliente chamado João Silva

```python
# crie manualmente e depois liste todos os clientes
```

![Resolução - Desafio 2](assets/images/Desafio%202.png)

### 🔹 3. Buscar um cliente pelo nome

```python
# utilize filter ou get
```

![Resolução - Desafio 3](assets/images/Desafio%203.png)


### 🔹 4. Criar dois novos produtos

- Teclado - R$ 150,00
- Monitor - R$ 800,00

```python
# depois liste todos os produtos cadastrados
```

![Resolução - Desafio 4](assets/images/Desafio%204.png)

### 🔹 5. Criar um pedido para João Silva com 1 Teclado

```python
# relacione usando objetos reais (ForeignKey)
```

![Resolução - Desafio 5](assets/images/Desafio%205.png)

### 🔹 6. Listar todos os pedidos de João Silva

```python
# use cliente.pedido_set.all()
```

![Resolução - Desafio 6](assets/images/Desafio%206.png)

### 🔹 7. Mostrar todos os produtos com preço acima de R$ 500,00

```python
# use filter com __gt
```

![Resolução - Desafio 7](assets/images/Desafio%207.png)

### 🔹 8. Mostrar quantos pedidos existem no sistema

```python
# use count()
```

![Resolução - Desafio 8](assets/images/Desafio%208.png)

### 🔹 9. Listar os pedidos ordenados pela data de criação (mais recente primeiro)

```python
# use order_by('-criado_em')
```

![Resolução - Desafio 9](assets/images/Desafio%209.png)

### 🔹 10. (Desafio extra) Calcular o total de produtos vendidos por nome

```python
# dica: use annotate + values
```

![Resolução - Desafio 1-](assets/images/Desafio%2010.png)

---

## 📢 Entrega

- Faça os testes no shell e tire print das saídas principais ou mostre em sala.

---

💡 Dica: A documentação do ORM é sua aliada!  
🔗 https://docs.djangoproject.com/pt-br/stable/topics/db/queries/

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Bons estudos e boas consultas com Django ORM! 🐍