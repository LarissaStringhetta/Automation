from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login")

    # Encontrar os elementos de input
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Teste de login com sucesso
    username_input.send_keys("student")
    password_input.send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(5)

    # Verificar se o login foi bem-sucedido
    success_message = "Logged In Successfully"
    assert success_message in driver.page_source, f"Login não foi bem-sucedido. Mensagem esperada: '{success_message}'"

    # Fechar o navegador ao final do teste
    driver.quit()