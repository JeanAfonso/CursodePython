valor = float(input('Qual o valor do Imovel? R$ '))
salario = float(input('Qual o valor do seu Salario? R$ '))
anos = int(input('Em quantos anos voce pretende pagar: '))
prestacao = valor / (anos * 12)
print(f'A prestação do imovel de R${valor} é de R${round(prestacao, 2)} com pagamento em {anos} anos')

if prestacao <= salario * 30 / 100:
    print('Parabens, seu financiamento foi aprovado!')
else:
    print('Sua parcela excede os 30% do seu salario, portanto nao podemos aprovar seu financiamento!')
