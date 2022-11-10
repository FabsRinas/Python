ano = int(input("Digite seu ano de nascimento: "))
idade = (2021 - ano)
print("Quem nasceu em {} está com {} em 2021".format(ano, idade))
if idade <9:
    print("CLASSIFICAÇÃO: MIRIM")
elif idade > 9 and idade <= 14:
    print("CLASSIFICAÇÃO: INFANTIL")
elif idade > 14 and idade <= 19:
    print("CLASSIFICAÇÃO: JÚNIOR")
elif idade > 19 and idade <= 25:
    print("CLASSIFICAÇÃO: SÊNIOR")
else:
    print("CLASSIFICAÇÃO: MASTER")
