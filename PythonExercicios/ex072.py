numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezoito', 'dezenove', 'Vinte' )

num = int(input('Digite um numero de 0 a 20: '))
while num > 20 or num < 0:
    num = int(input('Valor INVALIDO!! Digite Novamente: '))
print(f'O numero {num} por extenso é {numeros[num]}')