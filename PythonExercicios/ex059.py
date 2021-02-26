from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maiormenor = []
while opcao != 5:
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Maior\n'
          '[ 4 ] Novos numeros\n'
          '[ 5 ] SAIR')
    opcao = int(input('Qual é a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        multi = n1 * n2
        print(f'{n1} x {n2} = {multi}')
    elif opcao == 3:
        maiormenor.append(n1)
        maiormenor.append(n2)
        print(f'Entre {n1} e {n2} o maior valor é {max(maiormenor)}')
    elif opcao == 4:
        print('informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opcao Invalida. Tente novamente!')
    print('-=-' * 10)
    sleep(2)
print('FIM DO PROGRAMA!')