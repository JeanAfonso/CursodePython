larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensao de {larg}x{alt} e sua area é de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, voce precisara de {tinta}l de tinta')