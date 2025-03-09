from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

class cadastro_auto:
    def __init__(self):
        self.df = pd.read_excel(r"C:\Users\gsuti\OneDrive\Projetos\python\Selenium\Meu-sistema\Notas pendentes.xlsx")
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8501/")

    def cadastro(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            contrato_input = wait.until(EC.presence_of_element_located((By.ID, "text_input_1")))
            contrato_input.clear()
            contrato_input.send_keys(Keys.BACKSPACE * 20)
            contrato_input.send_keys(self.contrato)
            nota_input = wait.until(EC.presence_of_element_located((By.ID, "text_input_2")))
            nota_input.clear()
            nota_input.send_keys(Keys.BACKSPACE * 20)
            nota_input.send_keys(self.numero_nota)
            quantidade_input = wait.until(EC.presence_of_element_located((By.ID, "number_input_3")))
            quantidade_input.clear()
            quantidade_input.send_keys(Keys.BACKSPACE * 20)
            quantidade_input.send_keys(self.quantidade)
            valor_input = wait.until(EC.presence_of_element_located((By.ID, "number_input_4")))
            valor_input.clear()
            valor_input.send_keys(Keys.BACKSPACE * 20)
            valor_input.send_keys(self.valor)
            botao_cadastrar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="stBaseButton-secondary"]')))
            botao_cadastrar.click()
        except Exception as e:
            print("Erro")

    def pegar_valores(self): 
        # Iterar sobre as linhas do DataFrame
        for index, row in self.df.iterrows():
            self.contrato = row['Contrato']
            self.numero_nota = row['Nota']
            self.quantidade = row['Quantidade']
            self.valor = row['Valor Total']
            self.cadastro()

cadastro = cadastro_auto()
cadastro.pegar_valores()