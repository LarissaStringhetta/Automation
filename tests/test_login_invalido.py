from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_invalido():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login")

    # Encontrar os elementos de input
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Teste de login com usuário inválido
    username_input.send_keys("stud")
    password_input.send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(5)

    # Verificar se a mensagem de erro é exibida corretamente.
    error_message = "Your username is invalid!"
    assert error_message in driver.page_source, f"Login não foi bem-sucedido. Mensagem esperada: '{error_message}'"

    # Fechar o navegador ao final do teste
    driver.quit()