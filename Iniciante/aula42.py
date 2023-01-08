frase = 'aa aabbbcc'.lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    aparicao_letras = frase.count(frase[i])

    if frase[i] == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < aparicao_letras:
        qtd_apareceu_mais_vezes = aparicao_letras
        letra_apareceu_mais_vezes = frase[i]

    i += 1

    
print(f'A letra que apareceu mais vezes foi: {letra_apareceu_mais_vezes}, com um total de {qtd_apareceu_mais_vezes} vezes.')