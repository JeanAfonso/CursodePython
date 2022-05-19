from math import floor, ceil, trunc

num = float(input('Digite um numero flutuante: '))
inteiro = floor(num)
print(f'O numero inteiro de {num} é {inteiro}')

num1 = float(input('Digite um numero flutuante: '))
inteiro1 = ceil(num1)
print(f'O numero inteiro de {num1} é {inteiro1}')

num2 = float(input('Digite um numero flutuante: '))
inteiro2 = trunc(num2)
print(f'O numero inteiro de {num2} é {inteiro2}')