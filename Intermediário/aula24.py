# List comprehension em Python
# é uma forma rápida para criar listas
# a partir de iteráveis.

# lista = []

# for numero in range(10):
#   lista.append(numero)
# print(lista)

# O código acima é o mesmo que:
# usando list comprehension

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
