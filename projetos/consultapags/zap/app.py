import openpyxl
from urllib.parse import quote
import webbrowser

workbook = openpyxl.load_workbook('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\zap\\clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    mensagem = f'Ola {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%y')}. Favor pagar no link'

    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsapp)

    input('')