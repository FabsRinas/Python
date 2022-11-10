media = 0
velho = 0
nova = 0
for p in range(1, 5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(p)))
    idade = int(input("Digite a idade: "))
    sex = (str(input("Digite o sexo (M/F): "))).strip().upper()
    media += idade
    if sex == 'M':
        if idade > velho:
            velho = idade
            nomev = nome
    elif idade < 20:
        nova += 1
media = media/4
print("A média de idade do grupo é {}".format(media))
print("O nome do homem mais velho é {}".format(nomev))
print("A quantidade de mulheres mais nova que 20 anos é {}".format(nova))
