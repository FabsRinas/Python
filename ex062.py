primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}".format(termo), end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais gostaria de mostrar?: "))
print("fim")
