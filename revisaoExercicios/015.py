km_percorridos = float(input('Qual a quantidade de KM percorridos: '))
dias_aluguel = int(input('Voce alugou o carro por quantos dias? '))

preco_aluguel = 60 * dias_aluguel
preco_km = 0.15 * km_percorridos

print(f'O valor a pagar pelo aluguel do carro é de R$ {preco_aluguel+preco_km:.2f}')