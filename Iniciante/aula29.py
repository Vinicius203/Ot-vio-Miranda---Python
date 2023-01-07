'''
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero = input("Entre com um número e irei dobrar seu valor: ")

try:
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}.')
except:
    print('Isso não é um número.')