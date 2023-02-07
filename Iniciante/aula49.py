lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# Faça
lista_b = lista_a.copy()
# Ao invés de
# lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)