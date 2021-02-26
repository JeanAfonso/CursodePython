salario = float(input('Digite o Salario do funcionario R$ '))

if salario <= 1250.00:
    print(f'Quem ganhava R${salario}, passa a ganhar R${salario * 15 / 100 + salario}')
else:
    print(f'Quem ganhava R${salario}, passa a ganhar R${salario * 10 / 100 + salario}')