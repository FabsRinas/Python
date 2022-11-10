num = [[], []]
dado = 0
for c in range (1,8):
    dado = int(input(f"Digite o {c}º número: "))
    if dado % 2 == 0:
        num[0].append(dado)
    else:
        num[1].append(dado)
num[0].sort()
num[1].sort()
print('-=' * 30)
print(f'Os números pares digitados foram {num[0]}')
print(f'Os números ímpares digitados foram {num[1]}')
