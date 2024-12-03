from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

# 1 - Entrar no site https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&id_bairro%5B%5D=3187&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4
driver = webdriver.Chrome()
driver.get('https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&id_bairro%5B%5D=3187&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4')


# 2 - Inserir o preco, link da casa, data dentro de uma planilha q eu criei
# 3 - Anotar os precos, links das casas e datas de cada um dos anuncios daquela pagina
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links = driver.find_elements(By.XPATH, "//a[@class='carousel-cell is-selected']")

workbook = openpyxl.load_workbook('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\imoveis\\imoveis.xlsx')
pagina_imoveis = workbook['precos']

for preco, link in zip(precos, links):
    preco_formatado = (preco.text.split(' ')[1])
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%y')
    pagina_imoveis.append([preco_formatado,link_pronto,data_atual])

workbook.save('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\imoveis\\imoveis.xlsx')
# 4 - Se houver mais paginas, fazer o mesmo nas outras paginas
