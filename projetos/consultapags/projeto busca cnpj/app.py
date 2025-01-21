import PySimpleGUI as sg

sg.theme('reedit')

#Layout
tela_login = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*',key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(35,10))]
]

janela = sg.Window('Login', layout=tela_login)
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = values['usuario']
        senha_digitada = values['senha']
        print('passo1... feito')
        print('passo2... feito')
        print('passo3... feito')