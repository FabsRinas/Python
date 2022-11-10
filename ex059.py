n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
opc = 0
while opc != 5:
    print("""     [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa""")
    opc = int(input("Digite a opção desejada: "))
    if opc == 1:
        soma = n1+n2
        print("A soma dos números deu {}".format(soma))
    elif opc == 2:
        mult = n1*n2
        print("A multiplicação dos números deu {}".format(mult))
    elif opc == 3:
        if n1 > n2:
            print("O maior número é {}".format(n1))
        else:
            print("O maior número é {}".format(n2))
    elif opc == 4:
        n1 = int(input("Digite um novo número: "))
        n2 = int(input("Digite outro número: "))
    else:
        opc = 5
print("Programa finalizado")
