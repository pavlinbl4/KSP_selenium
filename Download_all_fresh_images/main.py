from credentials import get_credentials
from selenium.webdriver.common.by import By
from selenium import webdriver

from crome_options import setting_chrome_options

# авторизация на главной странице
def autorization():
    browser = webdriver.Chrome(options=setting_chrome_options())
    login, password, first_loggin = get_credentials()
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.NAME, "loginbtn").click()


if __name__ == '__main__':
    # авторизация на главной странице
    autorization()
