dia = int(input("Quantos dias alugado? :"))
km = float(input('Quantos KM rodados? :'))
pdia = 60*dia
pkm = km*0.15
tot = pdia+pkm
print('O total a pagar pelo carro alugado é R${:.2f}.'.format(tot))
