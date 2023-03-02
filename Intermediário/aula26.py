# List comprehension em Python
# é uma forma rápida para criar listas
# a partir de iteráveis.

# lista = []

# for numero in range(10):
#   lista.append(numero)
# print(lista)

# O código acima é o mesmo que:
# usando list comprehension
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] * 1.05 > 10 and produto['preco'] >= 20
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
p(novos_produtos)
