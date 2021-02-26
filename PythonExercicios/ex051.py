termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = termo1 + (10 - 1) * razao
for pa in range(termo1, decimo + razao, razao):
    print(f'{pa}', end=' -> ')
print('ACABOU')