'''
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))
'''
# é o mesmo que:

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print()

lista = [
    [letra for letra in 'Luiz']
    for y in range(3)
]

print(lista)
