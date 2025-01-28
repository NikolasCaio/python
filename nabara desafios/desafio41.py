nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}.'.format(nota1, nota2))
if media < 5:
    print('Sua media foi {:.1f},  REPROVADO.'.format(media))
elif media <= 6.9:
    print('Sua media foi {:.1f}, esta em recuperacao'.format(media))
else:
    print('sua media foi {:.1f}, voce esta aprovado!!'.format(media))
