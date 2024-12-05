from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
# 1 - Entrar no site https://consulta-empresa.netlify.app/
chrome_options = Options()
chrome_options.add_experimental_option('prefs',{
    # nao pedir permissao para download
    'download.prompt_for_download': False,
    #setar local padrao para armazenar downloads
    'download.default_directory': r'C:\Users\thale\Documents\Estudos\python\projetos\consultapags\projeto relatorio empresa\relatorios',
    # nao pedir permissao para realizar multipos downloads
    'profile.default_content_settings_values.automatic_downloads': 1
})
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://consulta-empresa.netlify.app/')
sleep(5)


# 2 - Fazer o login(clicar no campo usuario, digitar o usuario, clicar no campo senha, digitar a senha e clicar em entrar)
usuario = driver.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
usuario.click()
usuario.send_keys('jhonatan')


senha = driver.find_element(By.XPATH, "//input[@id='password']")
sleep(1)
senha.click()
senha.send_keys('12345678')

botao_entrar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg']")
botao_entrar.click()
sleep(5)


# 3 - Baixar o pdf de cada empresa e apos isso, renomear cada um deles para o nome da empresa do qual aquele relatorio pertence
def baixar_relatorios_das_empresas(driver):
     # 3.1 - Extrair o nome de cada empresa e guardar isso(numa lista)
    nomes_empresas = driver.find_elements(By.XPATH, "//td[@name='nome_empresa']")
    sleep(2)
    botao_download_pdf = driver.find_elements(By.XPATH, "//button[@class='download-btn']")
    sleep(2)

    for nome, botao_pdf in zip(nomes_empresas, botao_download_pdf):
        # Renomear o arquivo  de "perfil_empresa.pdf" para "nome_empresa.pdf"
        # 3.2 - A cada momento que eu baixar um arquivo, vou renomear ele para o nome daquela empresa
        botao_pdf.click()
        sleep(2)
        # Aguardo o download finalizar
        # Pego o nome do arquivo antigo e mudo para nome_da_empresa.pdf

        diretorio = r'C:\Users\thale\Documents\Estudos\python\projetos\consultapags\projeto relatorio empresa\relatorios'       
        nome_antigo = 'perfil_empresa.pdf'
        novo_nome = f'{nome.text}.pdf'

        caminho_completo_antigo = os.path.join(diretorio, nome_antigo)
        caminho_completo_novo = os.path.join(diretorio, novo_nome)

        os.rename(caminho_completo_antigo, caminho_completo_novo)
# 4 - Repetir o passo 3 ate baixar todos os pdf
baixar_relatorios_das_empresas(driver=driver)
botao_proxima_pagina = driver.find_element(By.XPATH, "//button[@id='nextBtn']")

while botao_proxima_pagina.get_attribute('disabled') == None:
    botao_proxima_pagina.click()
    baixar_relatorios_das_empresas(driver=driver)


