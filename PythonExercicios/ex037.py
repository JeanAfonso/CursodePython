num = int(input('Digite um numero inteiro: '))
print(''' Escolha umas das Bases de conversão
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''' )
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]} ')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print((f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}'))
else:
    print('Opção invalida! Digite novamente!')