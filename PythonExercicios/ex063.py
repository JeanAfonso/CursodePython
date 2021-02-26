N = int(input('Digite o primeiro numero inteiro: '))
F = 0
Fa = 1
while N >= 0:
    print(f'{F} -> ', end='')
    F = F + Fa
    Fa = F - Fa
    N -= 1
print('Acabou!')
