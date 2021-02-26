peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2
print(f'Seu IMC é {round(imc, 2)}')
if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <= 24.9:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA!!!')
