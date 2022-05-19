produto = float(input('Digite o valor para calcular o  seu desconto(5%) R$: '))

desconto = (produto * 5) / 100

print(f'o valor do desconto é de R$ {desconto:.2f} e o valor a pagar é de R$ {produto - desconto:.2f}')