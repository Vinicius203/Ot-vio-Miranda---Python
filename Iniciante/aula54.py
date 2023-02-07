'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes de listas
'''

import os
lista = []

while True:
    option = input('Escolha uma opção:\n[I]nserir [A]pagar [L]istar [S]air: ')

    if option.lower() == 's':
        break

    elif option.lower() == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)

    elif option.lower() == 'l':
        if(len(lista) == 0):
            print('A lista está vazia.')
        
        for nome, indice in enumerate(lista):
            print(nome, indice)

    elif option.lower() == 'a':
        if(len(lista) == 0):
            print('A lista está vazia! Não há nada para apagar')
        else:
            indice = input('Qual indice deseja apagar? ')   
            del lista[indice]
            
    else:
        print('Por favor, escolha uma opção válida.')

