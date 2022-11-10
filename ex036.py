casa = float(input("Digite o valor da casa: R$"))
sal = float(input("Digite o seu salário: R$"))
fin = int(input("Quantos anos de financiamento?"))
pres = casa/(fin*12)
if pres >= (sal*0.3):
    print("Para pagar uma casa de R${:.2f} em {} anos,".format(casa, fin))
    print("A prestação será de {:.2f}, empréstimo NEGADO.".format(pres))
else:
    print("Para pagar uma casa de R${:.2f} em {} anos,".format(casa, fin))
    print("A prestação será de {:.2f}, empréstimo APROVADO".format(pres))
