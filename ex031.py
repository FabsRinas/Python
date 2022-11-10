dist = float(input('Digite a distância de sua viagem (KM):' ))
if dist <= 200:
    prec = dist * 0.5
    print('A sua viagem irá custar R${:.2f} (R$0.50/KM)'.format(prec))
else:
    prec = dist * 0.45
    print('A sua viagem irá custar R${:.2f} (R$0.45/KM)'.format(prec))
