salario = float(input('Digite um salario: '))

if salario > 1250:
    aumento = salario * 10 / 100
    salario += aumento
    print(f'Voce teve um aumento de 10% R$ {aumento:.2f}, '
          f'e seu salario atual é de R$ {salario:.2f}')
else:
    aumento = salario * 15 / 100
    salario += aumento
    print(f'Voce teve um aumento de 15% R$ {aumento:.2f}, '
          f'e seu salario atual é de R$ {salario:.2f}')