n1 = int(input('Numero q voce deseja ver o dobro o triplo e a raiz quadrada '))
d = n1 * 2
t = n1 * 3
r = n1 ** 2
print('O dobro e \033[0;30m{} \n \033[m o triplo e \033[0;36m{} \n \033[m e o quadrado e \033[1;35m{} \033[m'.format(d, t,r))