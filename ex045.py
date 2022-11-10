from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Escolha uma opção: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
opcao = int(input("Escolha uma jogada: "))
if comp == 0:
    if opcao == 0:
        print("EMPATE")
    elif opcao == 1:
        print("GANHOU")
    elif opcao == 2:
        print("PERDESTE")
elif comp == 1:
    if opcao == 0:
        print("PERDESTE")
    elif opcao == 1:
        print("EMPATE")
    elif opcao == 2:
        print("GANHOU")
elif comp == 2:
    if opcao == 0:
        print("GANHOU")
    elif opcao == 1:
        print("PERDESTE")
    elif opcao == 2:
        print("EMPATE")
