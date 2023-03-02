# dir, hasattr e getattr em Python
# dir -> cita os métodos
# hasattr -> verifica se a varíavel possui o método
# getattr -> pega o método

string = 'Vinicius'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo:', metodo)
