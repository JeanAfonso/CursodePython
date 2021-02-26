from random import randint
num = tuple((randint(0, 1000)) for i in range(5))
print(f'Dos valores gerados {num}, O maior valor gerado foi {max(num)} e o menor valor gerado foi {min(num)}')