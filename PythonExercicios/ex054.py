from datetime import date
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if date.today().year - ano < 21:
        menor += 1
print(f'Ao todo tivemos {menor} menores de idade e {c - menor} maiores de idade')