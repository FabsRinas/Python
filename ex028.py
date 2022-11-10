from random import randint
pc = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente advinhar.')
jog = int(input('Em que número o computador pensou? '))
if jog == pc:
    print('Parabéns, você advinhou o número {} corretamente!'.format(pc))
else:
    print('Ganhei, pois eu pensei no número {}'.format(pc))
print('Obrigado por participar!')
