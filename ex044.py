comp = float(input("Digite o valor das compras: R$"))
print('''FORMAS DE PAGAMENTO: 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais cartão''')
opcao = int(input("Qual a opção? : "))
if opcao == 1:
    tot = comp - (comp * 0.1)
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(comp, tot))
elif opcao == 2:
    tot = comp - (comp * 0.05)
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(comp, tot))
elif opcao == 3:
    print("Sua compra vai custar R${:.2f}".format(comp))
elif opcao == 4:
    tot = comp + (comp * 0.2)
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(comp, tot))
else:
    print("Opção inválida")
