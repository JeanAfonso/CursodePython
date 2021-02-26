nome = str(input('Digite seu nome: ')).strip().lower()
letras = nome.count('a')
pos = nome.find('a') +1
pos2 = nome.rfind('a') +1
print(f'A letra A aparece {letras}x na frase')
print(f'A primeira letra A apareceu na posiçao {pos}')
print(f'A ultima letra A apareceu na posiçao {pos2}')
