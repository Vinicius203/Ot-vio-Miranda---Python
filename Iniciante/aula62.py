# teste
# cpf = 36440847007

# Primeiro Dígito
import re
import sys

cpf = input('Entre com o seu cpf (APENAS NUMEROS): ')

# cpf = cpf.replace('.', '') \
#    .replace('-', '')

cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

contador_cpf = 0
aux = 10

for i in range(0, 9):
    contador_cpf += int(cpf[i]) * aux
    aux -= 1

digito_1 = (contador_cpf * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

# Segundo Dígito

aux_2 = 11
contador_cpf = 0

for i in range(0, 10):
    contador_cpf += int(cpf[i]) * aux_2
    aux_2 -= 1

digito_2 = (contador_cpf * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

print(
    f'O valor do primeiro digíto do seu CPF é {digito_1}, e o do segundo dígito é {digito_2}.')

cpf_codigo = cpf[0:9] + str(digito_1) + str(digito_2)

if cpf_codigo == cpf:
    print('O CPF é válido.')
else:
    print('CPF INVÁLIDO.')
