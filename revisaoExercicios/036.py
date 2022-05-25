casa = float(input('Valor da casa: '))
salario = float(input('Digite seu Salario: '))
anos = int(input('Em quantos anos vai pagar: '))

prestacao = casa / (anos * 12)
limite = salario * 0.30
parcelas = anos * 12

if prestacao > limite:
    print('Emprestimo negado, o valor da sua '
          f'prestacao é de R$ {prestacao:.2f} e excedeu 30% do seu '
          f'salario R$ {limite:.2f}')

else:
    print(f'Emprestimo aprovado! Voce pagara R$ {casa:.2f} em '
          f'{parcelas} parcelas '
          f'de R$ {prestacao:.2f}.')
