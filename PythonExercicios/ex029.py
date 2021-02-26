velocidade = float(input('Em qual velocidade o carro está: '))

if velocidade <= 80:
    print(f'Você esta dentro da velocidade permitida! {velocidade}Km/h')
else:
    print(f'Você esta acima da velocidade permitida de 80 Km/h e foi multado em R$ {(velocidade - 80)*7.00}')