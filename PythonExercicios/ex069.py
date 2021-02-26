man = women = people = 0
print('-='*20)
print('CADASTRO DE PESSOAS')
print('-='*20)
while True:
    years = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo:[M/F] ')).upper().strip()[0]
        if years >= 18:
            people += 1
        if sex == 'M':
            man += 1
        if sex == 'F' and years < 20:
            women += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if option == 'N':
        break
print(f'Pessoas com com mais de 18 anos: {people}')
print(f'Homens Cadastrados: {man}')
print(f'Mulheres com menos de 20 anos: {women}')




