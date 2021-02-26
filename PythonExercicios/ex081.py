numeros = []
option = 'S'
while option in 'Ss':
    numeros.append(int(input('Digite um numero: ')))
    option = str(input('Deseja continuar? [S/N] ')).upper().strip()
print(f'Voce digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem Decrescente são {numeros}')
if 5 in numeros:
    print('O numero 5 esta na lista.')
else:
    print('O numero 5 não foi digitado.')