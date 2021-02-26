#Exemplo 1 (if, else)

nome = str(input('Digite seu nome: '))
if nome == 'Jean':
    print('Seu lindo')
else:
    print(f'Bom dia {nome}')

#Exemplo 2 (Elif)

idade = int(input('Digite sua Idade: '))
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Adulto')