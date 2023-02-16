# Exercício com funções

# Crie uma função que multiplica todos
# os argumentos não nomeados recebidos
# Retorne o total para uma variável e 
# mostre o valor da variável.

def multiplica(*args):
    r = 1
    for numero in args:
        r *= numero
    return r

r = multiplica(1, 2, 3, 4, 5)
print(r)

# Crie uma função que fala se o número é
# par ou ímpar. Retorne se o número é par
# ou ímpar.
import random

def parImpar(x):
    r = 'Par' if x % 2 == 0 else 'Ímpar'
    print(f'O número gerado foi: {x}.')
    return r

r = parImpar(random.randint(0, 100))
print(r)