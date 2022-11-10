ano = int(input("Digite seu ano de nascimento: "))
idade = (2021 - ano)
print("Quem nasceu em {} está com {} em 2021".format(ano, idade))
if idade > 18:
    print("O tempo de alistamento excedeu em {} ano(s)".format(idade-18))
elif idade == 18:
    print("Você poderá se alistar este ano")
else:
    print("Você poderá se alistar em {} ano(s)".format(18-idade))
