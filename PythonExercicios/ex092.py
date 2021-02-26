from datetime import datetime

info = dict()
info['nome'] = str(input('Nome: ')).capitalize()
nasc = int(input('Ano de Nascimento: '))
info['idade'] = datetime.now().year - nasc
info['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if info['ctps'] != 0:
    info['contratacao'] = int(input('Ano de contratação: '))
    info['salario'] = float(input('Salário: R$'))
    info['aposentadoria'] = info['idade'] + ((info['contratacao'] + 35) - datetime.now().year)

print('-='*30)
for k, v in info.items():
    print(f' - {k} tem o valor {v}')
