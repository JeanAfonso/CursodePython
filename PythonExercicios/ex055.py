lista = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    lista.append(peso)
print(f'A pessoa mais pesada tem {max(lista)}Kg e a pessoa mais leve tem {min(lista)}Kg')