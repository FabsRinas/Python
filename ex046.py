from time import sleep
print("Se preparem para a queima de fogos!")
tempo = 10
for c in range (0, 10):
    print("{}!".format(tempo))
    tempo = tempo - 1
    sleep(1)
print("FELIZ ANO NOVO!!")
