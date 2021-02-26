n = soma = total = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    total += 1
    soma += n
    n = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {total} numeros e a soma dos valores digitados é {soma}')
