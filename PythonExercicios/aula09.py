frase = '  Curso em Video Python  '
print(frase[0:26])
print(frase.count('o'))
print(frase.upper().count('O')) #pode ser lower no lugar de upper.
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #para mudar o valor de um string nesse caso uso frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Curso')) #Ele mostra onde começa a palavra curso no index, se nao existir ele traz -1
print(frase.split()) #dividido = frase.split()
#print(dividido[3])

