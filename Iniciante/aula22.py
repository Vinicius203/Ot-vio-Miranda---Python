# Operadores lógicos
# and / or / not
# None = não valor, DIFERENTE DE 0/NULO

'''
entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha):
    print('Você entrou no sistema.')
else:
    print('Você NÃO entrou.')
'''

# Avaliação de curto circuito

print(False or False or 0 or 'abc')

senha = input('Senha: ') or 'Sem senha'
print('A senha não foi digitada.')

