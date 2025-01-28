import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} \n tem o SENO {:.2f} \n e o cosseno de {:.2f} \n e o tangente de {:.2f}'.format(angulo,seno, cosseno, tangente ))