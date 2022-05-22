velocidade = int(input('Digite a velocidade: '))
limite = 80

if velocidade <= limite:
    print('Dentro da velocidade permitida.')
else:
    multa = (velocidade - limite) * 7
    print(f'Voce ultrapassou o limite de velocidade em '
          f'{velocidade - limite} km/h e será multado em R$ {multa:.2f}')