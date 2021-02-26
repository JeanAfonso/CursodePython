valores = []
option = 'S'
while option in 'Ss':
    num = int(input('Digite um numero: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso.')
    elif num in valores:
        print('Valor duplicado não sera adicionado.')
    option = str(input('Quer continuar [S/N]: ')).upper().strip()
print(f'Os valores digitados foram {sorted(valores)}')
