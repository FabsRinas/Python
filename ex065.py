opt = "s"
tot = cont = maior = 0
menor = 99999
while opt == "s":
    num = int(input("Digite um número: "))
    tot += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opt = str(input("Quer continuar? [S/N]: "))
med = tot / cont
print("Você digitou {} números e a média deles foi {:.2f}".format(cont, med))
print("O maior foi {} e o menor foi {}".format(maior, menor))
