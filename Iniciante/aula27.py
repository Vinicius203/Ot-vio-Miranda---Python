# Fatiamento de Strings
# Fatiamento [inicio:final:passo] [::]
# Obs: a função len retorna o tamanho da str (quantidade de caracteres)

# Olá mundo
# 012345678

variavel = 'Olá mundo'
print(len(variavel))
print(variavel[4:8])
print(variavel[4:])
print(variavel[:8])
print(variavel[0:len(variavel):2])