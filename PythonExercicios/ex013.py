salario = float(input('Qual o salario do funcionario?R$'))
reajuste = int(input('Quanto de reajuste?'))
calc = salario + (salario * reajuste / 100)
print('O salario que antes era de R${:.2f},com um reajuste de {}% agora e de R${:.2f}'.format(salario, reajuste, calc))