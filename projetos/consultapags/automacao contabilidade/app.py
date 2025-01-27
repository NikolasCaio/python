from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# Iniciar o navegador
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

# Preencher o e-mail
email = driver.find_element(By.XPATH, "//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')

# Preencher a senha
senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(2)
senha.send_keys('contabilidade123456')

# Clicar no botão "Entrar"
botao_entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
sleep(2)
botao_entrar.click()

# Ir diretamente para a página de registro
sleep(2)
driver.get('https://contabilidade-devaprender.netlify.app/registration.html')
sleep(3)

# Abrir a planilha de dados
empresas = openpyxl.load_workbook('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\automacao contabilidade\\empresas.xlsx')
pagina_empresas = empresas['dados empresas']

# Iterar pelas empresas na planilha
for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, email_empresa, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha

    # Preencher os campos da página
    driver.find_element(By.ID, 'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID, 'emailEmpresa').send_keys(email_empresa)
    sleep(1)
    driver.find_element(By.ID, 'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID, 'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID, 'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID, 'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID, 'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID, 'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    # Clicar no botão "Cadastrar"
    driver.find_element(By.ID, 'Cadastrar').click()
    sleep(3)

# Fechar o navegador
driver.quit()
