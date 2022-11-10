p = h = m = 0
while True:
    print("CADASTRE UMA PESSOA")
    print("======================")
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()
    if idade > 18:
        p = p + 1
    if sexo == "F" and idade < 20:
        m = m + 1
    if sexo == "M":
        h = h + 1
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {p}")
print(f"Total de homens: {h}")
print(f"Total de mulheres com menos de 20 anos: {m}")
