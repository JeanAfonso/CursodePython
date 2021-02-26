alunos = []
boletim = []
media = []
option = 'S'
while option in 'Ss':
    alunos.append(str(input('Nome do aluno: ')).strip().capitalize())
    alunos.append(float(input('1ª Nota: ')))
    alunos.append(float(input('2ª Nota: ')))
    media.append((alunos[:][1] + alunos[:][2]) / 2)
    boletim.append(alunos[:])
    alunos.clear()
    option = str(input('Deseja continuar? [S/N] ')).upper()
    if option in 'Nn':
        break

print(f'{" BOLETIM DA CLASSE ":-^30}')
print(f'{"Nº"}| {"NOME":^15} | {"MÉDIA":>8}')
print('-' * 30)
for p in range(len(boletim)):
    print(f'{p} | {boletim[p][0]:^15} | {media[p]:>8}')
print()

while True:
    indiv = int(input('Digite o Nº do Aluno para ver suas notas (999 Termina): '))
    if indiv != 999:
        print()
        print(f'Aluno Nº {indiv} | Nome: {boletim[indiv][0]} | Notas: {boletim[indiv][1:]} | Média: {media[indiv]}')
        print()
    else:
        print('Programa Terminado!')
        break