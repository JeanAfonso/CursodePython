from time import sleep
from random import randint

print('-=-'*20)
print('VAMOS JOGAR JOKENPO?')
print('-=-'*20)

print('ESCOLHA\n'
      ' [ 1 ] PEDRA!\n'
      ' [ 2 ] PAPEL!!\n'
      ' [ 3 [ TESOURA!!')
jogador = int(input('Digite sua jogada: '))
if jogador > 3:
    print('Jogada INVALIDA, tente novamente dentro das opcões.')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

computador = randint(1, 3)
print(computador)

if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Vence')
    elif jogador == 3:
        print('Computador vence')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Jogador Empate')
    elif jogador == 3:
        print('Jogador vence')
    else:
        print('jogada invalida')
elif computador == 3:
    if jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    elif jogador == 3:
        print('Empate')
    else:
        print('jogada invalida')

