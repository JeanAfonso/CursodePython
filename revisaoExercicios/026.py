frase = input('Digite uma frase: ').strip().upper()
busca = frase.count('A')
posicao = frase.find('A') + 1
ultima_posicao = frase.rfind('A') + 1
print(busca)
print(posicao)
print(ultima_posicao)
