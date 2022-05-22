n1 = int(input('reta 1: '))
n2 = int(input('reta 2: '))
n3 = int(input('reta 3: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Essas retas podem formar um triangulo!')
else:
    print('Nao pode ser um triangulo!')