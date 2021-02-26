sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Dados Invalidos, digite novamente e use apenas M para Masculino ou F para Feminino.')
    sexo = str(input('Digite novamente seu sexo [M/F]: ')).upper().strip()
print(f'O sexo escolhido é {sexo} e foi e Registrado com Sucesso.')
