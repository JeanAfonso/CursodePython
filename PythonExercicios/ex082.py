pares = []
impares = []
option = 'S'
while option in 'Ss':
    num = int(input('Digite um numero: '))
    option = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'A lista completa é {pares + impares}')
print(f'Os numeros pares são {pares}')
print(f'Os numeros impares são {impares}')


