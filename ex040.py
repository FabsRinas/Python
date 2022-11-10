n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2)/2
if media >= 7:
    print("APROVADO COM A MÉDIA DE {:.2f}".format(media))
elif media < 7 and media >= 5:
    print("RECUPERAÇÃO COM A MÉDIA DE {:.2f}".format(media))
else:
    print("REPROVADO COM MÉDIA DE {:.2f}".format(media))
