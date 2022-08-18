import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from crome_options import setting_chrome_options
from selenium.webdriver.common.alert import Alert
from dotenv import load_dotenv
import os
from kommersant_dates import KommersantDates
from bs4 import BeautifulSoup

# import credentials
load_dotenv()
login = os.environ.get('login')
password = os.environ.get('password')
first_loggin = os.environ.get('first_loggin')

report_web_link = 'https://image.kommersant.ru/photo/archive/pubhistory.asp?ID='


def autorization():  # авторизация на главной странице
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#au').send_keys('Евгений Павленко')


def select_today_published_images():
    autorization()
    time.sleep(1)

    try:
        alert = Alert(browser)
        alert.accept()
        time.sleep(2)
    finally:
        select = Select(browser.find_element(By.NAME, 'ps'))
        select.select_by_value('50')

        select = Select(browser.find_element(By.ID, "dt"))  # select "засыла"
        select.select_by_value("3")

        data_input = browser.find_element(By.ID, "since")
        data_input.clear()
        data_input.send_keys(yesterday)

        data_input = browser.find_element(By.ID, "till")
        data_input.clear()
        data_input.send_keys(yesterday)

        browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()

        try:
            alert = Alert(browser)
            alert.accept()
            time.sleep(2)
        finally:

            return browser.page_source


def publication_info(k, count):
    report_link = f'{report_web_link}{k}#web'
    browser.get(report_link)
    print(report_link)
    report_html = browser.page_source

    soup = BeautifulSoup(report_html, 'lxml')
    all_publications = soup.find(id='Table1').find('tbody').find_all('tr')
    image_info = {}

    for i in range(len(all_publications)):
        try:
            if yesterday in all_publications[i].find_all('td')[8].text:  # date of upload
                print(f"{count} - {soup.find('h3').text}")
                image_info['A'] = count
                image_info['B'] = soup.find('h3').text[16:]
                print(f"date of publication - {all_publications[i].find_all('td')[2].text}")  # date of publication
                image_info["C"] = all_publications[i].find_all('td')[2].text
                print(f"publication - {all_publications[i].find_all('td')[3].text}")  # publication
                image_info["D"] = all_publications[i].find_all('td')[3].text

                print(f"material - {all_publications[i].find_all('td')[5].text}")  # material
                image_info["E"] = all_publications[i].find_all('td')[5].text

        finally:
            continue

    print()
    return image_info


def end():
    browser.close()
    browser.quit()


browser = webdriver.Chrome(options=setting_chrome_options())
yesterday = KommersantDates().yesterday
