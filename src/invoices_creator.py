from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class InvoiceCreator:
    def __init__(self, driver_path=None, download_dir="downloads"):
        chrome_options = Options()
        prefs = {
            "download.default_directory": os.path.abspath(download_dir),  # Diretório de download
            "download.prompt_for_download": False,  # Não perguntar onde salvar
            "download.directory_upgrade": True,  # Atualizar o diretório automaticamente
            "plugins.always_open_pdf_externally": True  # Abrir PDFs fora do navegador
        }
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    
    def create_invoice(self, url, invoice_data):
        try:
            self.driver.get(url)
            time.sleep(3)  

            # Iterar sobre os dados da fatura e preencher os campos
            for field in invoice_data:
                xpath = field.get("xpath")  # XPath do campo
                value = field.get("value")  # Valor a ser preenchido
                if xpath and value:
                    self.driver.find_element(By.XPATH, xpath).send_keys(value)

            # Salva arquivo
            button = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/div[2]/div[3]/button')
            ActionChains(self.driver).move_to_element(button).click().perform()


            time.sleep(10)  # Aguarde o processamento
        except Exception as e:
            print(f"Erro ao criar a fatura: {e}")
        finally:
            self.driver.quit()