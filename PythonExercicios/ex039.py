from datetime import date

sexo = int(input('Digite seu sexo - 1 para Feminino e 0 para Masculino: '))

if sexo == 1:
    print('Você nao precisa se alistar, pois o alistamento é obrigatorio somente para Homens.')
else:
    print('Continue preenchendo')

nasc = int(input('Digite o ano de seu nascimento: '))
data = date.today().year
alist = data - nasc

print(f'Quem nasceu em {nasc} tem {alist} em {data}')


if alist == 18:
    print(f'Voce tem que se alistar IMEDIATAMENTE')
elif alist < 18:
    saldo = 18 - alist
    ano = data + saldo
    print(f'Você ainda não completou 18 anos restam {saldo} anos')
    print(f'Seu alistamento sera em {ano}')
elif alist > 18:
    saldo = alist - 18
    ano = data - saldo
    print(f'Ja passou da hora de se alistar, você deveria ter se alistado a {saldo} ano(s)')
    print(f'Voce deveria ter se alistado em {ano}')

