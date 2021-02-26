viagem = float(input('Qual é a distacia de sua viagem? '))
print(f'Você esta prestes a começar uma viagem de {viagem}Km')

if viagem <= 200:
    print('E o preço da sua passagem será de R$', viagem * 0.50)
else:
    print('E o preço da sua passagem é de R$', viagem * 0.45)