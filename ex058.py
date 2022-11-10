from random import randint
comp = randint(0,10)
cont = 0
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar?")
acertou = False
pal = int(input("Digite um palpite: "))
while not acertou:
    if pal == comp:
        acertou = True
    else:
        if pal < comp:
            pal = int(input("Mais alto: "))
            cont += 1
        elif pal > comp:
            pal = int(input("Mais baixo: "))
            cont += 1
print("Parabéns! você acertou em {} tentativas!".format(cont))
