preco = float(input('Preço das compras R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] A vista no dinheiro ou cheque
[ 2 ] A vista no cartão debito
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão de crédito''')

opcao = int(input('Qual é a opção? '))
if opcao > 4:
    print('Opcão Invalida, tente novamente.')

if opcao == 1:
    print(f'A vista no dinheiro a sua compra de R$ {round(preco, 2)}, sai por R$ {preco - preco * 10 / 100} com 10% de desconto.')
elif opcao == 2:
    print(f'A vista no cartão a sua compra de R$ {round(preco, 2)}, sai por R$ {preco - preco * 5 / 100} com 5% de desconto.')
elif opcao == 3:
    print(f'Em 2x de R$ {preco / 2} no cartão a sua compra de R$ {round(preco, 2)}, sai por R$ {round(preco, 2)} sem juros.')
elif opcao == 4:
    parcelas = int(input('Escolha o numero de parcelas: '))
    if parcelas <= 2:
        print('Para este numero de parcelas escolha as opções anteriores.')
    else:
        total = preco + preco * 20 /100
        print(f'Sua compra parcelada em {parcelas}x de R$ {total / parcelas} embutido juros de 20%, totaliza um valor de R$ {round(total, 2)} ')