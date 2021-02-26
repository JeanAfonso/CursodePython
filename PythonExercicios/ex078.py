lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um numero na posiçao {c}: ')))
print(f'Os valores digitados foram {lista}')
print(f'O maior valor digitado foi {max(lista)} na posiçao ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print(f'e o menor valor digitado foi {min(lista)} na posiçao ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')