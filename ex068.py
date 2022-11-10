from random import randint
vit = 0
while True:
    comp = randint(0, 10)
    valor = int(input("Digite um valor entre 0 e 10: "))
    escolha = ' '
    total = comp + valor
    while escolha not in "PI":
        escolha = str(input("Par ou impar? (P/I): ")).strip().upper()
    print(f"Você jogou {valor} e o computador jogou {comp}, totalizando {total}")
    if escolha == "P":
        if total % 2 == 0:
            print("Venceu!")
            vit = vit + 1
        else:
            print("Perdeu, otário.")
            break
    elif escolha == "I":
        if total % 2 == 1:
            print("Venceu!")
            vit = vit + 1
        else:
            print("Perdeu, otário.")
            break
print(f"você conseguiu {vit} antes de perder, parabéns!")
