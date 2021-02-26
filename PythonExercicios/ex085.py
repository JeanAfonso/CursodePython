numeros = [[], []]

for p in range(7):
    num = int(input(f'Digite o {p+1}ª numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Os numeros Pares digitados foram {sorted(numeros[0])}')
print(f'Os numeros Inpares digitados foram {sorted(numeros[1])}')