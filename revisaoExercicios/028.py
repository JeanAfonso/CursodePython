from random import randint

pc = randint(0, 5)

eu = int(input('Escolha um numero de 0 a 5: '))

if eu == pc:
    print('Você acertou!')
else:
    print('você errou, tente novamente!')