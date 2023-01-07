a = 'AAA'
b = 'BBBB'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)

# ou, com f-Strings

print(f'A = {a}, B = {b}, C = {c:.2f}')