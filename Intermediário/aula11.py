pessoa = {}

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE!')
else:
    print(pessoa['sobrenome'])

