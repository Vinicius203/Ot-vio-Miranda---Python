# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica


duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))
