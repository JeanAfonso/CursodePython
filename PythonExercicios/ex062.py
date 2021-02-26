primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressao finalizada com {total} termos mostrados.')
