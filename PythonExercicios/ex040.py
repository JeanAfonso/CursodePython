n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é {media}')
if media >= 7.0:
    print('APROVADO')
elif media >= 5.0 <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO!')