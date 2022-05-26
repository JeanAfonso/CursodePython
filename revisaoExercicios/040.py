nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f'Sua media foi {media}, e é maior que 7.0, APROVADO!')
elif media >= 5.0 <= 6.9:
    print(f'Sua media foi de {media}, é maior que 5.0 e menor que 6.9'
          f'.RECUPERACAO')
else:
    print(f'Sua media foi de {media}, é menor que 5.0. REPROVADO!')

