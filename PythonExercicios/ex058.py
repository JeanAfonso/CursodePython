from random import randint

cont = 0
print('Tente advinhar o numero que o Computador escolheu de 0 a 10.')
pc = randint(0, 10)
numero = int(input('Digite seu palpite: '))
while numero != pc:
    cont += 1
    if numero < pc:
        print(f'Mais... Digite seu palpite novamente')
        numero = int(input('Seu palpite novamente: '))
    if numero > pc:
        print(f'Menos... Digite seu palpite novamente')
        numero = int(input('Digite seu palpite novamente: '))
print(f'Parabens você acertou! Você escolheu {numero} e o Computador escolheu {pc}, e foram necessarias {cont} Tentativas.')
