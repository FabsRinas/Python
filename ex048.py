soma = 0
num = 0
print("Eu lhe mostrarei a soma dos números ímpares divisiveis por 3 de 1 a 500: ")
for c in range(0, 500):
    if (c % 3) == 0:
        if (c % 2) == 1:
            num = num + 1
            soma = soma + c
print("A soma dos {} valores deu {}".format(num, soma))
