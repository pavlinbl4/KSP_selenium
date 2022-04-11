"""
по заданному ключевому слову определяет количество моих снимков в архиве
и сохраняет ссылку на результаты поиска
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from os import getenv

login = getenv('login')
password = getenv('password')
first_loggin = getenv('first_loggin')

if not login:
    exit("no login provided")


def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # фоновый режим
    # chrome_options.add_argument('--no-sandbox')  # не понятная мне опция, отключаю
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    return chrome_options


def get_image_links(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[9]
    tbody = table.find('tbody')
    images_links = tbody.find_all(title="Добавить кадрировку")
    return images_links


def autorization(keyword):  # авторизация гна главной странице
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#text').send_keys(keyword)
    browser.find_element(By.CSS_SELECTOR, '#au').send_keys('Евгений Павленко')
    # browser.find_element(By.CSS_SELECTOR, '#lib0').click()  # исключаю из поиска KP снимки !!!!
    select = Select(browser.find_element(By.NAME, 'ps'))
    select.select_by_value('100')
    browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()
    images_number = browser.find_element(By.CSS_SELECTOR,
                                         'body > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > b:nth-child(1)').text
    print(images_number)  # количество моих снимков, найденных по данному ключевому слову

    # print(browser.current_url[:-1]) # обрезаю последнюю букву для дальнейшей пагинации
    print(browser.current_url)
    time.sleep(5)
    browser.close()
    browser.quit()


keyword = 'ярмарка'

if __name__ == '__main__':
    browser = webdriver.Chrome(options=setting_chrome_options())
    autorization(keyword)
