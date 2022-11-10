termo = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = 0
n2 = termo
while c < 10:
    print("{}".format(n2), end=" ")
    n2 = n2 + r
    c += 1
print("fim")
