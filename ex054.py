from datetime import date
atual = date.today().year
totmai = 0
totmen = 0
for p in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmai += 1
    else:
        totmen += 1
print("{} pessoas atingiram a maior idade e {} não atingiram ainda".format(totmai, totmen))
