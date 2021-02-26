'''for c in range(0, 6): #no python ele sempre para no ultimo numero, se for conta de 1 até 6 fazer range de (1, 7) ou a partir de 0.
    print('oi')
print('fim')'''

'''for c in range(6, 0, -1): # se quiser conta de tras pra frente adicionar o -1 no final do range.
    print(c)
print('fim')''

for c in range(0, 7, 2): # se quiser que ele conte de 2 em 2 adicionar o 2 ou mais no final.
    print(c)
print('fim')

n = int(input('Digite um valor: ')) #eu posso usar o range para pegar de um numero até o numero da minha variavel, ex: de 0 até o numero que eu escolher na minha variavel.
for c in range(0, n+1):
    print(c)
print('Fim')
R

#Posso usar no Range as minhas variaveis, o i representa inicio, f fim e p passo, posso comecar de uma variavel até outra e pular numeros pela ultima variavel colocada no range ex(inicio, fim, pula)
i = int(input('Valor: '))
f = int(input('valor: '))
p = int(input('valor: '))
for c in range(i, f+1, p)
    print(c)
print('FIM')

#Para pedir a definicao de uma variavel quantas vezes eu quiser.
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')'''

# Se eu quiser o somatorio de todos os numeros que eu digitei.
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma de todos os valores foi {s}')