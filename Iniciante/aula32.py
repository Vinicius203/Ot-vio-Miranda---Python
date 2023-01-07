"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


num = input('Entre com um número inteiro: ')

'''
if num.isdigit():
    num_int = int(num)
    if(num_int % 2 == 0):
        print(f'O número {num_int} é par.')
    else:
        print(f'O número {num_int} é impar.')
else:
    print('A entrada não é um número inteiro.')
'''
try:
    num_int = int(num)
    if(num_int % 2 == 0):
        print(f'O número {num_int} é par.')
    else:
        print(f'O número {num_int} é impar.')
except:
    print('A entrada não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora em números inteiros: ')

try:
    hora_int = int(hora)

    if(hora_int >= 18 and hora_int <= 23):
        print('Bom dia!')
    elif (hora_int > 11 and hora_int <= 17):
        print('Boa tarde!')
    else:
        print('Bom dia!')
except:
    print('O valor de entrada não é um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Entre com o seu nome: ')

if(len(nome) <= 4):
    print('Seu nome é curto.')
elif(len(nome) > 6):
    print('Seu nome é muito grande.')
else:
    print('Seu nome é normal.')