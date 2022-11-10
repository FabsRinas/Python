cont = 0
soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f"Foram digitados {cont} números e a soma deles deu {soma}")
