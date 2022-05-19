n = int(input('Digite o numero para ver a sua tabuada: '))

if n >= 0:
    for x in range(1, 11):
        print(f'{n} x {x} = {n * x}')
else:
    print('0 x 0 é igual a 0')
