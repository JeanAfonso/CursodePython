lista = []
genero = 0
anos = 0
for people in range(1, 5):
    print("-=-"*10)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F/M: ')).upper()
    anos += idade
    if sexo != 'M' and idade < 20:
        genero += 1
    elif sexo == 'M':
        lista.append(idade)

print(f'A média de idade do grupo é {(anos / people)}')
print(f'Neste grupo apenas {genero} mulheres tem menos de 20 anos')
print(f'O homem mais velho do grupo tem {max(lista)} anos e o mais novo tem {min(lista)} anos.')
