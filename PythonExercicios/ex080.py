numeros = []
for c in range(5):
    num = int(input('Digite um numero: '))
    for key, value in enumerate(numeros):
        if num < value:
            numeros.insert(key, num)
            print(f'Numero adicionado a posição {key} da lista')
            break
    else:
        numeros.append(num)
        print('Numero adicionado ao fim da lista...')
print(f'Os valores digitados foram ordenados {numeros}')

# metodo do professor
''' lista = [] 
for c in range (0, 5):
    n = int(input('digite um numero: ') 
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...'
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')'''