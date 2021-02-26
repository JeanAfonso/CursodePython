# Listas

num = [2, 3, 4, 7, 9]
num[2] = 3
num.append(10)
num.sort(reverse=True)
num.insert(2, 1) #insere um numero na posicão desejada (pos, numero)
num.pop() # elimina o ultimo elemento da lista
#if 1 in num:
 #   num.remove(1)
#else:
#    print('Numero nao encontrado')
#print(num)

a = [0, 1, 2, 3, 4]
b = a[:] #usando [:] voce copia os valores de a para b, assim da para mudar b sem alterar a
b[2] = 8 #altera o valor do indice 2 para 8

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')