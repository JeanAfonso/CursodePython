num = tuple(int(input('Digite o {}º numero: '.format(n+1))) for n in range(4))
nove = num.count(9)
print(f'Os valores digitados são: {num}')
print(f'O numero 9 aparece {nove} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
print('O(s) numero(s) pares digitado(s) foi(foram): ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end='...')
