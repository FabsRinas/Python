print("10 termos de uma PA")
termo = int(input("Digite o primeiro termo: "))
p = int(input("Digite a razão: "))
fim = termo + (10 - 1) * p
for c in range (termo, fim, p):
    print('{}'.format(c), end=' ')
print("Acabou")
