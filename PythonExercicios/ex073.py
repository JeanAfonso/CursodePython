posicions = ('Flamengo', 'Palmeiras', 'Santos', 'Sao Paulo', 'Internacional', 'Corinthians', 'Gremio', 'Athletico PR', 'Bahia', 'Goias', 'Vasco', 'Atletico', 'Botafogo',
             'Fortaleza', 'Ceara', 'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
for times in posicions:
    print(times)

print(f'Os 5 primeiros colocados são {posicions[0:5]}')
print(f'Os 4 ultimos colocados no famoso Z-4 são {posicions[16:20]}')
print(sorted(posicions))
print(f'A Chapecoense se encontra na {posicions.index("Chapecoense")}° Colocação')