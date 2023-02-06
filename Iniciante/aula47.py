'''
Listas em Python
tipo list - Mutável
suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar  Ler  Alterar Apagar = lista[i] (CRUD)
'''

lista = [10, 20, 30, 40, 50]
lista[2] = 300
print(lista)

del lista[2]
print(lista)

lista.append(60)
lista.append(70)
print(lista)
ultimo_valor = lista.pop() # remove último item da lista
print(lista, '/ Removido: ', ultimo_valor)