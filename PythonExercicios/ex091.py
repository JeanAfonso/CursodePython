from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
cont = 0
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(0, 6)

print('Valores Sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')

print('-=' * 15)
print('<< RANKING DE JOGADORES >>')
print('-=' * 15)

for k in sorted(jogadores, key=jogadores.get, reverse=True):
    cont += 1
    sleep(0.7)
    print(f"{cont}° lugar: {k} com {jogadores[k]} ")

# ESSA RESOLUCÁO DO PROFESSOR GUANABARA PARA ENTENDER ITEMGETTER

jogo = dict(jogador1=randint(1, 6), jogador2=randint(1, 6), jogador3=randint(1, 6), jogador4=randint(1, 6))
ranking = list()
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('<< RANKING DE JOGADORES >>')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)