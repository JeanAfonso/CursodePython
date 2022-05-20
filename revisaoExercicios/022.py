nome = input('Digite o nome completo: ').strip()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
primeiro = nome.split()
print(len(primeiro[0]))