# TUPLAS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # Tuplas são Imutaveis.

#del(lanche) <- apaga a tupla
for comida in lanche:                   # maneira mais simples se nao precisar saber a posiçao
    print(f'Eu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}') # fazendo dessa maneira vou trazer os nomes no seu respectivo len

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')


print('Comi pra caramba!')