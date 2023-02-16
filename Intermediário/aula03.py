def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)


soma(100, 200)
soma(7, 9, 0)

# Quando o argumento de Z não for chamado,
# a função irá usar o valor padrão como
# substituto (nesse caso, None)
