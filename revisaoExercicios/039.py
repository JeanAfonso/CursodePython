from datetime import datetime

sexo = int(input('digite seu sexo: 1 - Feminino e 0 para Masculino: '))

if sexo == 1:
    print('Alistamento é obrigatorio somente para o sexo Masculino.')
else:
    print('prossiga')

idade = int(input('Digite o ano de nascimento: '))
data = datetime.now().year
ano = data - idade

if ano == 18:
    print('Você deve se alistar esse ano.')

elif ano < 18:
    saldo = 18 - ano
    alistamento = data + saldo
    print(f'Voce ainda não tem idade para se alistar. '
          f'Voce devera se alistar em {saldo} anos, em {alistamento}.')

elif ano > 18:
    saldo = ano - 18
    alistamento = data - saldo
    print(f'Voce ja deveria ter se alistado a {saldo} anos, em {alistamento}.')

