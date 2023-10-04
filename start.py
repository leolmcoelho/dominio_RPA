from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService

import pyautogui
import time


def element(driver, tag: str, time: int = 15, method: str = 'xpath'):

    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable((method, tag)))
    element = driver.find_element(method, tag)

    return element
service = ChromeService(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

def start():
    # Configurar o driver do Chrome
    # Substitua pelo caminho do seu chromedriver
    

    # Acessar a página de login
    driver.get("https://www.dominioweb.com.br/")

    # Encontrar o campo de usuário e preenchê-lo
    username_field = element(driver, '//*[@id="trid-auth"]/form/label[1]/span[2]/input')
    username_field.send_keys("leandro_teza@hotmail.com")  # Substitua pelo seu nome de usuário

    # Encontrar o campo de senha e preenchê-lo
    password_field = element(driver, '//*[@id="trid-auth"]/form/label[2]/span[2]/input')
    password_field.send_keys("Teza2024@@@@@")  # Substitua pela sua senha

    # Enviar o formulário de login
    password_field.send_keys(Keys.ENTER)

    # Aguarde alguns segundos para que a página de login seja processada
    # driver.implicitly_wait(10)

    # Verifique se o login foi bem-sucedido (você pode usar algum elemento na página de destino para verificar)
    time.sleep(5)
    pyautogui.hotkey('right')
    time.sleep(1)

    # Pressione Enter
    pyautogui.press('enter')


# Feche o navegador
# driver.quit()
# input('Start')
if __name__ == '__main__':
    start()
