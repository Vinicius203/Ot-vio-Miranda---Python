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
        
        for indice, nome in enumerate(lista):
            print(indice, nome)

    elif option.lower() == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Esse índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    else:
        print('Por favor, escolha uma opção válida.')

