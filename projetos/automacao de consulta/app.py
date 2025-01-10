from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import openpyxl

numero_oab = 259155
planilha_dados_consulta = openpyxl.load_workbook('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\automacao de consulta\\dados_de_processos.xlsx')
pagina_processos = planilha_dados_consulta['processos']

# 1 - Entrar no site https://pje-consulta-publica.tjmg.jus.br/
driver = webdriver.Chrome()
driver.get("https://pje-consulta-publica.tjmg.jus.br/")
sleep(3)

# 2 - Clicar no campo de oab e digitar o numero do advogado
campo_numero_oab = driver.find_element(By.XPATH,"//input[@id='fPP:Decoration:numeroOAB']")
sleep(1)
campo_numero_oab.click()
sleep(1)
campo_numero_oab.send_keys(numero_oab)

# 3 - selecionar o estado daquele advogado
selecao_uf = driver.find_element(By.XPATH,"//select[@id='fPP:Decoration:estadoComboOAB']")
sleep(1)
opcao_uf = Select(selecao_uf)
sleep(1)
opcao_uf.select_by_visible_text('SP')
sleep(1)

# 4 - Clicar em pesquisar
campo_pesquisar = driver.find_element(By.XPATH,"//input[@id='fPP:searchProcessos']")
sleep(1)
campo_pesquisar.click()
sleep(3)

# 5 - Entrar em cada um dos precessos e extrair numero do advogado, numero do precesso e nome dos participantes
links_abrir_processos = driver.find_elements(By.XPATH,"//a[@title='Ver Detalhes']")

for link in links_abrir_processos:
    janela_principal = driver.current_window_handle
    link.click()
    sleep(3)
    janelas_abertas = driver.window_handles
    for janela in janelas_abertas:
        if janela not in janela_principal:
            driver.switch_to.window(janela)
            sleep(1)
            numero_processo = driver.find_elements(By.XPATH,"//div[@class='propertyView ']//div[@class='col-sm-12 ']")[0]
            sleep(1)
            participantes = driver.find_elements(By.XPATH,"//tbody[contains(@id,'processoPartesPoloAtivoResumidoList:tb')]//span[@class='text-bold']")
            lista_participantes = []
            for participante in participantes:
                lista_participantes.append(participante.text)

            if len(lista_participantes) == 1:
                pagina_processos.append([numero_oab,numero_processo.text,lista_participantes[0]])
            else:
                pagina_processos.append([numero_oab,numero_processo.text,','.join(lista_participantes)])
            planilha_dados_consulta.save('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\automacao de consulta\\dados_de_processos.xlsx')
            driver.close()
# 6 - Salvar os dados para uma planilha
# 7 - Repetir ate finalizar todos os processos daquele advogado
    driver.switch_to.window(janela_principal)