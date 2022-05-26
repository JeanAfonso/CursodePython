from datetime import datetime

nasc = int(input('Data de nascimento: '))
data = datetime.now().year
ano = data - nasc

print(ano)

if ano <= 9:
    print('MIRIM')
elif ano <= 14:
    print('INFANTIL')
elif ano <= 19:
    print('JUNIOR')
elif ano <= 25:
    print('SENIOR')
else:
    print('MASTER')