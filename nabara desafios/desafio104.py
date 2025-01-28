from time import sleep
c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2
     '\033[0;30;43m', # 3
     '\033[0;30;44m', # 4
     '\033[0;30;45m', # 5
     '\033[0;30;46m', # 6
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end=" ")
    help(com)
    print(c[0], end=" ")
    sleep(2)



def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end=" ")
    print('-'* tam)
    print(msg)
    print('-'* tam)
    print(c[0], end=" ")
    sleep(1)



comando = ''
while True:
    titulo('Sistema de ajuda pyHELP', 2)
    comando = str(input('Funcao ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('ate logo!', 1)
