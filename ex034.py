sal = float(input('Digite o seu salário: R$'))
if sal <=1250.00:
    aum = sal + (sal*0.15)
    print('Você passará a receber de R${} para R${} com 15% de aumento'.format(sal, aum))
else:
    aum = sal + (sal*0.1)
    print('Você passará a receber de R${} para R${} com 10% de aumento'.format(sal, aum))
