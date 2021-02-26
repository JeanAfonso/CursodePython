from random import sample, shuffle
#primeira maneira de se fazer sorteio organizado
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]

sorteio = sample(lista, k=4) #k = o numero de pessoas dentro da lista que serao sorteadas.

print(f'A ordem das pessoas sorteadas é,', sorteio)

#segunda maneira de fazer o sorteio

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem das pessoas sorteadas é', lista)
