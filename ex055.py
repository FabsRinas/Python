maior = 0
menor = 1000
for p in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa (Kg): ".format(p)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O mais pesado possui {}kgs e o mais leve possui {}kgs".format(maior, menor))
