'''teste = list()
teste.append('Jean')
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera)'''

'''galera = [['joao', 19], ['Ana', 33], ['Pedro', 20], ['Carlos', 25]]
print(galera)
for p in galera:
    print(p[0]) # printa somente os nomes nesse caso
    print(p[1]) # printa somente a idade'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
