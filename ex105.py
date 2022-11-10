def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos
    :param sit: Valor opcional para dizer ou não a situação
    :return: Dicionário com várias informações dos alunos
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if r['media'] > 7:
        r['situação'] = 'BOA'
    elif r['media'] >= 5:
        r['situação'] = 'RAZOÁVEL'
    else:
        r['situação'] = 'RUIM'

    return r


resp = notas(5.5, 2.5, 10, 8.5, 10, sit=True)
print(resp)
help(notas)
