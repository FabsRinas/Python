num = int(input("Digite um número inteiro: "))
print('''Escolha uma destas opções para converter o número:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
conv = int(input("Sua opção: "))
if conv == 1:
    print("O número {} em binário é igual a {}".format(num, bin(num)[2:]))
elif conv == 2:
    print("O número {} em octal é igual a {}".format(num, oct(num)[2:]))
elif conv == 3:
    print("O número {} em hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida.")
