from random import randint
count = 0
victory = 0
print('-='*20)
print('JOGO DO PAR OU IMPAR')
print('-='*20)
while True:
    pc = randint(0, 10)
    n = int(input('Digite um valor: '))
    count = pc + n
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar?[P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {pc}, a soma dos valores foi {count}. ', end='')
    print('Deu PAR' if count % 2 == 0 else 'Deu IMPAR')
    if pi == 'P':
        if count % 2 == 0:
            print('Você VENCEU! Jogue novamente!')
            victory += 1
        else:
            print(f'Você PERDEU!! ', end='')
            break
    elif pi == 'I':
        if count % 2 == 1:
            print('Você VENCEU! Jogue novamente!')
            victory += 1
        else:
            print(f'Você PERDEU!! ', end='')
            break
print(f'Você venceu {victory} vezes!')