'''
Iterando strings com While
'''

nome = 'Vinicius Martins Freire'
novo_nome = ''
i = 0
tamanho = len(nome)

while i < tamanho:
    novo_nome += '*' + nome[i]
    i += 1

novo_nome += '*'
print(novo_nome)