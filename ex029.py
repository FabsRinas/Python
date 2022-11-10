vel = float(input('Digite a velocidade atual do carro (KM/H): '))
if vel >=80:
    multa = (vel - 80) * 7
    print('Você levará uma multa de {:.2f} reais por exceder 80 KM/h.'.format(multa))
else:
    print('Dirija com segurança e tenha um bom dia!')
