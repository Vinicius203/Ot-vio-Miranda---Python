# Geração de CPF

import random

cpf_nove = ''

for i in range(9):
    cpf_nove += str(random.randint(0, 9))

# Primeiro Dígito

contador_cpf = 0
aux = 10

for i in range(0, 9):
    contador_cpf += int(cpf_nove[i]) * aux
    aux -= 1

digito_1 = (contador_cpf * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

# Segundo Dígito

cpf_dez = cpf_nove + str(digito_1)
aux_2 = 11
contador_cpf = 0

for i in range(0, 10):
    contador_cpf += int(cpf_dez[i]) * aux_2
    aux_2 -= 1

digito_2 = (contador_cpf * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

print(
    f'O valor do primeiro digíto do seu CPF é {digito_1}, e o do segundo dígito é {digito_2}.')

cpf_codigo = cpf_nove[0:9] + str(digito_1) + str(digito_2)

print(cpf_codigo)
