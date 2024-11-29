from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


# 1 - Entrar no site - https://precos-de-produtos.netlify.app/
driver = webdriver.Chrome()
driver.get('https://precos-de-produtos.netlify.app/')
sleep(5)

# 2.1 - Rolar a pagina inteira para baixo para carregar os produtos 
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# 2.2 - Clicar em 'carregar mais' para visualizar o restante dos produtos
botao_carregar_mais = driver.find_element(By.XPATH, "//button[@id='loadMoreButton']")
sleep(2)
botao_carregar_mais.click()
sleep(2)
# 3 - Rolar a pagina totalmente para baixo
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)
# 4 - Subir totalmente de volta para o topo
driver.execute_script('window.scrollTo(0, 0);')
sleep(2)
# 5 - Clicar em subir planilha de precos
planilha_botao = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-custom']")
sleep(1)
planilha_botao.click()
sleep(1)
# 6 - Carregar planilha "precos-produtos-atualizados.xlsx"
pyautogui.write('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\preco_produtos\\precos-produtos-atualizados.xlsx')
sleep(2)
pyautogui.press('enter')
input('Aperte enter no terminal para fechar o progama')