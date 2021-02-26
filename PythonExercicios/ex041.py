from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
data = date.today().year

ano = data - nasc
print(f'O atleta tem {ano} anos.')

if ano <= 9:
    print(f'Classificação: MIRIM')
elif ano <= 14:
    print('Classificação: INFANTIL')
elif ano <= 19:
    print('Classificação: JUNIOR')
elif ano <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
