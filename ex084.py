pessoas = list()
dado = list()
maior = 0
menor = 0
resp = 's'
while resp == 's':
    dado.append(str(input("Digite o nome da pessoa: ")))
    dado.append(float(input("Digite o peso da pessoa (kgs): ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input("Quer continuar? [S/N]: ")).lower()
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior:.2f}. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {menor:.2f}. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
