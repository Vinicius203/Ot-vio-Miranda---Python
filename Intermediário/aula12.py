# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': ' Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)  # se não estiver a chave 'idade' no dict, o padrão será 0
print(pessoa['idade'])

# print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.values()))
print(list(pessoa.items()))

# for chave in pessoa.keys():
#   print(chave)

# for chave, valor in pessoa.items():
#   print(chave, valor)
