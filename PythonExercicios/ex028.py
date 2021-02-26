from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um numero de 0 a 5, tente adivinhar....')
print('-=-' *20)
numero = int(input('Digite um numero entre 0 e 5: '))
print('Processando....')
sleep(2.0)
if not -1 < numero <= 5:
    print('Numero Inválido')
elif computador == numero:
    print('VOCÊ ACERTOU!!!')
else:
    print(f'PERDEU!! Eu escolhi o numero {computador}')
