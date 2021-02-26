pessoas = {'nome': 'Jean', 'Sexo': 'M', 'idade': '29'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():  #não tem enumerate, preciso usar items
    print(f'{k} = {v}')
for k in pessoas.values():
    print(k)

pessoas['nome'] = 'Jean2' #posso tbm usar del para apagar del pessoas['Sexo']

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['Sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil: # Laço usado para lista
    for k, v in e.items(): # laço usado para dicionarios.
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()