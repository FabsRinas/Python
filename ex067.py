while True:
    num = int(input("Digite um valor para ver sua tabuada: "))
    if num < 0:
        break
    for c in range(1, 11):
        mult = num * c
        print(f"{num} x {c} = {mult}")
print("Fim")
