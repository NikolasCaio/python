aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovado'
print(aluno)
print('-='* 30)
for k, v in aluno.items():
    print(f'- {k} = {v}')
