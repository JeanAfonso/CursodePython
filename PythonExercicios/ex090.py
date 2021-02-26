aluno = dict()
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'A média de {aluno["Nome"]}: '))
if aluno["Média"] >= 7:
    aluno['Aprovacao'] = 'Aprovado'
else:
    aluno['Aprovacao'] = 'Reprovado'
print('-=' * 20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
