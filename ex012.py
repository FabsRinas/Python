pro = float(input('Digite o preço do produto: R$'))
des = pro/20
tot = pro-des
print('O produto que custava R${:.2f}, na promoção com 5% de desconto custará R${:.2f}.'.format(pro, tot))
