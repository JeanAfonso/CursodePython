lista = []
total = quant = media = 0
option = 'S'
while option in 'Ss':
    num = int(input('Digite um numero: '))
    option = str(input('Quer continuar [S/N]: ')).upper().strip()
    total += num
    quant += 1
    lista.append(num)
media = total / quant
print(f'Voce digitou {quant} numeros e a media foi {media}')
print(f'O maior numero digitado foi {max(lista)} e o menor numero foi {min(lista)}')
