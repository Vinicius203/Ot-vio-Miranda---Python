'''
enumerate - enumera iteráveis (índices)
'''

lista = ['Maria', 'João', 'Helena']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome)

# ou
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)