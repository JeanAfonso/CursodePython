n = int(input('Digite um numero para ver a sua tabuada: '))
for x in range(1,11):
 print('{:2} x {:2} = {:2}'.format(n,x,n*x))