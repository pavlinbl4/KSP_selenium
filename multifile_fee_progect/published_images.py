import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from dotenv import load_dotenv
import os
from scrap_publication_list import image_publications_voc
from checked_day_publications_only import checked_month_publications_only
from crome_options import setting_chrome_options

red = '\033[91m'
green = '\33[32m'
end = '\033[0m'

load_dotenv()
login = os.environ.get('login')
password = os.environ.get('password')
first_loggin = os.environ.get('first_loggin')

report_web_link = 'https://image.kommersant.ru/photo/archive/pubhistory.asp?ID='


def check_id_image(image_id):
    select = Select(browser.find_element(By.ID, "dt"))  # select "засыла"
    select.select_by_value("3")

    data_input = browser.find_element(By.ID, "since")
    data_input.clear()

    id_input = browser.find_element(By.ID, "code")
    id_input.clear()
    id_input.send_keys(image_id)

    browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()

    return browser.page_source


def end_selenium():
    browser.close()
    browser.quit()


def autorization():  # авторизация на главной странице
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#au').send_keys('Евгений Павленко')


def select_today_published_images(check_date):
    # autorization()
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
        data_input.send_keys(check_date)

        data_input = browser.find_element(By.ID, "till")
        data_input.clear()
        data_input.send_keys(check_date)

        browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()

        try:
            alert = Alert(browser)
            alert.accept()
            time.sleep(2)
        finally:

            return browser.page_source


def published_for_all_time(k):  # функция находит все опубликованные снимки из 'засыла' без фильтрации по датам
    report_link = f'{report_web_link}{k}#web'
    browser.get(report_link)
    report_html = browser.page_source
    publication_voc = \
        image_publications_voc(report_html)  # снимки из "засыла", которые были отмечены как опубликованные
    return publication_voc


def publication_info(k, count, check_date):
    publication_voc = published_for_all_time(k)  # получаю данные о всех публикациях данного снимка
    used_images = checked_month_publications_only(check_date, publication_voc, count)
    return used_images


browser = webdriver.Chrome(options=setting_chrome_options())
