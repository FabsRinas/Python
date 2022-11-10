resp = 's'
lista = []
while resp == 's':
    n = int(input("Digite um valor: "))
    if n not in lista:
        print("Valor adicionado")
        lista.append(n)
    else:
        print("Valor duplicado, não irei adicionar à lista")
    resp = str(input("Quer continuar? [S/N]: ")).lower()
lista.sort()
print(f"A sua lista ficou: {lista}")
