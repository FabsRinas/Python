total = totmil = menor = cont = 0
while True:
    produto = str(input("Digite o produto: "))
    preco = float(input("Digite o preço: R$"))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == "N":
        break
print("{:-^40}".format(" fim do programa "))
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato custa R${menor:.2f}")