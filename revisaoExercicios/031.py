viagem = int(input('Digite a distancia da viagem: '))

if viagem <= 200:
    preco = viagem * 0.50
    print(f'O preco da viagem é de R$ {preco}, km x 0.50')
else:
    preco = viagem * 0.45
    print(f'O preco da viagem é de R$ {preco}, km x 0.45')