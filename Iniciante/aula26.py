'''
Formatação de Strings - f-Strings
(Caractere) (><^) (Quantidade)
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}.')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel:0^10}.')
print(f'O hexadecimal de 1500 é {1500:08X}.')