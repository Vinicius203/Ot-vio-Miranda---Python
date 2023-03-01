# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#    print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.60,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args (já vimos) e kwargs
# kwargs - keyword arguments (argumentos nomeados)


def mostrar_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostrar_argumentos_nomeados(nome='Joana', qLq=123)
mostrar_argumentos_nomeados(**pessoas_completa)
