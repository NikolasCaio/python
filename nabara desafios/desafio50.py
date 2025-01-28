print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Primeiro termo: '))
r = int(input('Razao: '))
decimo = termo + (10-1) * r
for c in range(termo, decimo, r):
    print('{}'.format(c), end=' ==>')
print('Acabou!')