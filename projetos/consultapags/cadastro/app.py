import openpyxl
# import pyautogui
# import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Entrar na planilha
workbook = openpyxl.load_workbook('C:\\Users\\thale\\Documents\\Estudos\\python\\projetos\\consultapags\\cadastro\\produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
# Copiar informacao de um campo e colar no seu campo correspondente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for linha in sheet_produtos.iter_rows(min_row=2):
    driver.get('https://cadastro-produtos-devaprender.netlify.app/')
    
    nome_produto = linha[0].value
    botao_nome_do_produto = driver.find_element(By.XPATH, "//input[@id='product_name']")
    
    botao_nome_do_produto.click()
    botao_nome_do_produto.send_keys(nome_produto)

    descricao = linha[1].value
    botao_descricao = driver.find_element(By.XPATH, "//textarea[@id='description']")
    
    botao_descricao.click()
    botao_descricao.send_keys(descricao)
    

    categoria = linha[2].value
    botao_categoria = driver.find_element(By.XPATH, "//input[@id='category']")
    
    botao_categoria.click()
    botao_categoria.send_keys(categoria)
    
    codigo_produto = linha[3].value
    botao_codigo_produto = driver.find_element(By.XPATH, "//input[@id='product_code']")
    sleep
    botao_codigo_produto.click()
    botao_codigo_produto.send_keys(codigo_produto)
    

    peso = linha[4].value
    botao_peso = driver.find_element(By.XPATH, "//input[@id='weight']")
    
    botao_peso.click()
    botao_peso.send_keys(peso)
    

    dimensoes = linha[5].value
    botao_dimensoes = driver.find_element(By.XPATH, "//input[@id='dimensions']")
    
    botao_dimensoes.click()
    botao_dimensoes.send_keys(dimensoes)
    

    botao_proximo = driver.find_element(By.XPATH, "//button[@class='btn btn-primary me-2']")
    botao_proximo.click()
    

    preco = linha[6].value
    botao_preco = driver.find_element(By.XPATH, "//input[@id='price']")
    
    botao_preco.click()
    botao_preco.send_keys(preco)
    

    quantidade_em_estoque = linha[7].value
    botao_estoque = driver.find_element(By.XPATH, "//input[@id='stock']")
    
    botao_estoque.click()
    botao_estoque.send_keys(quantidade_em_estoque)
    

    data_de_validade = linha[8].value
    botao_data_de_validade = driver.find_element(By.XPATH, "//input[@id='expiry_date']")
    
    botao_data_de_validade.click()
    botao_data_de_validade.send_keys(data_de_validade)
    

    cor = linha[9].value
    botao_cor = driver.find_element(By.XPATH, "//input[@id='color']")
    
    botao_cor.click()
    botao_cor.send_keys(cor)
    

    tamanho = linha[10].value
    # Localizar o elemento <select>
    dropdown = driver.find_element(By.XPATH, "//select[@id='size']")
    valor_atual = dropdown.get_attribute('value')  # Obter o valor atual selecionado no dropdown
    # Double under

    # Se o valor atual for diferente do valor na planilha, altera
    if tamanho != valor_atual:  # 'tamanho' é o valor da planilha (linha[10].value)

        dropdown_tamanho = Select(dropdown)

        if tamanho == 'Pequeno':
            dropdown_tamanho.select_by_visible_text('Pequeno')
        elif tamanho == 'Médio':
            dropdown_tamanho.select_by_visible_text('Médio')
        elif tamanho == 'Grande':
            dropdown_tamanho.select_by_visible_text('Grande')

        
        
    material = linha[11].value
    botao_material = driver.find_element(By.XPATH, "//input[@id='material']")
    
    botao_material.click()
    botao_material.send_keys(material)

    # botao proximo da pagina 2
    botao_proximo2 = driver.find_element(By.XPATH, "//button[@class='btn btn-primary me-2']")
    botao_proximo2.click()

    fabricante = linha[12].value
    botao_fabricante = driver.find_element(By.XPATH, "//input[@id='manufacturer']")

    botao_fabricante.click()
    botao_fabricante.send_keys(fabricante)

    pais_origem = linha[13].value
    botao_pais_origem = driver.find_element(By.XPATH, "//input[@id='country']")

    botao_pais_origem.click()
    botao_pais_origem.send_keys(pais_origem)

    obsevacoes = linha[14].value
    botao_observacoes = driver.find_element(By.XPATH, "//textarea[@id='remarks']")

    botao_observacoes.click()
    botao_observacoes.send_keys(obsevacoes)

    codigo_de_barra = linha[15].value
    botao_codigo_de_barra = driver.find_element(By.XPATH, "//input[@id='barcode']")

    botao_codigo_de_barra.click()
    botao_codigo_de_barra.send_keys(codigo_de_barra)

    localizacao_armazem = linha[16].value
    botao_localizacao_armazem = driver.find_element(By.XPATH, "//input[@id='warehouse_location']")

    botao_localizacao_armazem.click()
    botao_localizacao_armazem.send_keys(localizacao_armazem)

    # botao concluir da ultima pagina
    botao_concluir = driver.find_element(By.XPATH, "//button[@class='btn btn-primary me-2']")
    botao_concluir.click()
    
    sleep(1)
    # botao de alerta do google
    alert = Alert(driver)
    alert.accept()
    # botao de adicionar mais um 
    sleep(1)
    botao_adicionar_mais_um = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    botao_adicionar_mais_um.click()

# Repetir esses passos para outros campos ate preencher campos daquela pagina
# Clicar em proxima
# Repetir os mesmos passos e ir para a proxima pagina(pagina 2)
# O cadastro daquele produto e clicar em concluir
# clicar em ok, para finalizar o processo
# clicar em ok mais uma vez na mensagem  de confirmcao do salvamento no banco de dados
# Clicar em adicionar mais um e repetir o "processo" ate finalizar a planilha
