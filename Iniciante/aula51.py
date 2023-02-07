'''
Introdução ao desempacotamento + tuples
'''

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)
# O underline (_) é uma convenção indicando que essa variável não será usada mais adiante no código

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)