sal = float(input('Digite o seu salário: R$'))
aum = sal*0.15
nsal = sal+aum
print('Um funcionário que ganhava R${:.2f} recebeu 15% de aumento, ganhando agora R${:.2f}'.format(sal, nsal))
