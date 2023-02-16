'''
Escopo de Funções
O escopo GLOBAL é onde todo o código é alcançável
O escopo LOCAL é onde apenas nomes do mesmo local 
podem ser alcançados.
'''

x = 1

def outer_scope():
    x = 10
    
    def inner_scope():
        x = 15
        print(x)

    inner_scope()

    print(x)

print(x)
outer_scope()
print(x)