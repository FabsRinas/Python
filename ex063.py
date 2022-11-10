print("SEQUÊNCIA DE FIBONACCI")
n = int(input("Quantos termos você quer mostrar? "))
c = 0
n1 = 0
n2 = 1
n3 = 0
print("{} {}".format(n1,n2), end=" ")
while c != (n-2):
    n3 = n1 + n2
    print("{}".format(n3), end=" ")
    n1 = n2
    n2 = n3
    c += 1
print("fim")