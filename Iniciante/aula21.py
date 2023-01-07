# Operadores lógicos
# and / or / not
# None = não valor, DIFERENTE DE 0/NULO

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha = '123456'

if (entrada == 'E') and (senha_digitada == senha):
    print('Você entrou no sistema.')
else:
    print('Você NÃO entrou.')

# True
print(True and True and True)

# False
print(True and False and True)

# 0
print(True and 0 and True)


