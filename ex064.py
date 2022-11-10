num = cont = tot = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    cont += 1
    tot = tot + num
    num = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} números e a soma deles deu {}".format(cont, tot))