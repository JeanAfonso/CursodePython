inteiro = int(input('Digite um numero: '))

print('Conversor de base numerica '
      'Digite 1 para binario, '
      '2 para octal e '
      '3 para hexadecimal')

option = int(input('Digite a Opcao: '))

if option == 1:
    print(f'O numero {inteiro} em binario é {bin(inteiro)}.')

elif option == 2:
    print(f'O numero {inteiro} em binario é {oct(inteiro)}.')

elif option == 3:
    print(f'O numero {inteiro} em binario é {hex(inteiro)}.')

else:
    print('opcao invalida.')

