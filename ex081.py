resp = 's'
lista = []
while resp == 's':
    n = int(input("Digite um valor: "))
    lista.append(n)
    resp = str(input("Quer continuar? [S/N]: ")).lower()
print(f'A quantidade de valores digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista e aparece {lista.count(5)} vezes')
else:
    print('5 não faz parte da lista')
