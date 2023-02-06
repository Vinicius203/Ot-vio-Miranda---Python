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

lista = [10, 20, 30, 40]
# lista.clear()
lista.insert(2, 'Dedé')  # Índice, Valor
print(lista)

lista_2 = ['a', 'b', 'c', 'd']
lista_3 = lista + lista_2
lista.extend(lista_2)
# O extend trabalha diretamente na lista, não é atribuido a uma nova variável
print(lista_3)
print(lista)
