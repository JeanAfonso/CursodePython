while True:
    n = int(input('Digite o numero para ver sua tabuada: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-='*20)
print('Programa encerrado!')