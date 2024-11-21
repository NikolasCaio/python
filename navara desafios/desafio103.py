def notas(*n, sit=False):
    """
   ---> Funcao para analisar notas e situacoes de varios alunos
    :param n: uma ou mais notas dos alunos(aceitavel)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA!'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 8.6, sit=True)
print(resp)
help(notas)
