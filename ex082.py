lista = []
par = []
impar = []
resp = 's'

while resp == 's':
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input("Quer continuar? [S/N]: ")).lower()

print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')
