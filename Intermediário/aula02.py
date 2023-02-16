'''
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''


def soma(x, y, z):
    print(x + y + z)


soma(1, 2, 3)  # não nomeado
soma(1, 2, z=5)  # nomeado
