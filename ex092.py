from datetime import datetime
trab = {}
trab['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
trab['idade'] = datetime.now().year - nasc
trab['cart'] = int(input("CTPS (0 se não possuir): "))
if trab['cart'] != 0:
    trab['contrato'] = int(input("Ano de contratação: "))
    trab['sal'] = float(input('Salário: R$'))
    trab['apos'] = trab['idade'] + ((trab['contrato'] + 35) - datetime.now().year)
print('-='*30)
for k, v in trab.items():
    print(f'  - {k} tem valor {v}')
