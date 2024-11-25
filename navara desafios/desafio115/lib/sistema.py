from interface import *
from time import sleep


cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('opcao 1')
    elif resposta == 2:
        cabecalho('opcao 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31mErro! DIGITE UMA OPCAO VALIDA!\033[m')
    sleep(1.5)