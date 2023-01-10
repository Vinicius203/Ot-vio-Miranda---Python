texto = 'Python s2'


'''
i = 0

while i < len(texto):
    print(texto[i])
    i += 1
'''

novo_texto = ''

for letra in texto:
    # novo_texto += letra + '*'
    novo_texto += f'*{letra}'
    print(letra)
    
print(novo_texto + '*')