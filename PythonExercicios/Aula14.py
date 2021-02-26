# a mesma funcionalidade For vs While sabendo o limite

for c in range(1, 10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# While sem saber o limite, ele vai me perguntar até que uma condiçao seja atendida, no caso ele para de pedir para digitar os numeros se eu colocar o '0', que é minha condiçao.

n = 1
while n != 0: #flag ou Ponto de parada.
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer Continuar?[S/N]: ')).upper()
print('Fim')

# Outro exemplo de programa

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares')