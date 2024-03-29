"""script download my published shoots to selected folder"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from credentials import get_credentials
from notification import system_notification
from tkinter import filedialog


def select_folder():
    choose_folder = filedialog.askdirectory(
        initialdir='/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency',
        title="Select your Source directory")
    if len(choose_folder) > 0:
        return choose_folder
    else:
        print("You don't choose folder. Program terminated")
        exit()


def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    return chrome_options


def enable_download():
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def make_shoot_edit_link(link):
    shoot_edit_link = f'https://image.kommersant.ru/photo{link[2:]}'
    return shoot_edit_link


def get_image_links(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[9]
    tbody = table.find('tbody')
    images_links = tbody.find_all(title="Добавить кадрировку")
    return images_links


def go_my_images(page_link) -> object:
    browser.get(page_link)
    html = browser.page_source
    return html


def main_cycle():
    range_number = images_number // 100 + 2  # количиство страниц выданных поиском
    for x in range(1, range_number):  # цикл по страницам съемки
        page_link = f'{shoot_link}2&pg={x}'  # ссылка на страницу с номером
        html = go_my_images(page_link)  # получаю html открытой страницы
        images_links = get_image_links(html)  # получаю список ссылок редактирование изображения
        print(f'на странице {x} - {len(images_links)} снимков')
        for i in range(len(images_links)):  # (len(images_links)):
            shoot_edit_link = make_shoot_edit_link(images_links[i].get('href'))
            browser.get(shoot_edit_link)
            browser.find_element(By.CSS_SELECTOR,
                                 f"div.hi-subpanel:nth-child(3) > a:nth-child(4)").click()


def images_number_in_shot():
    try:
        return int((browser.find_element(By.CSS_SELECTOR,
                                         'body > table:nth-child(6) '
                                         '> tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > '
                                         'table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > '
                                         'td:nth-child(1) > b:nth-child(1)').text).replace(' ', ''))
    except Exception as ex:
        print(ex)
        print('снимков с данным ключевым словом не найдено')
        return '0'


def create_folder():
    os.makedirs(f'{image_folder}/{shoot_id}', exist_ok=True)


def autorization():  # авторизация гна главной странице
    login, password, first_loggin = get_credentials()
    create_folder()  # создаю папку для скачивания снимков
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#code').send_keys(shoot_id)  # ввожу номер съемки
    select = Select(browser.find_element(By.NAME, 'ps'))
    select.select_by_value('100')
    browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()
    browser.save_screenshot(f'{image_folder}/{shoot_id}/Screen_short_{shoot_id}.png')  # создаю скриншот для проверки
    return browser.current_url[:-1]  # return shoot link


if __name__ == '__main__':
    shoot_id = input("input shoot id look like 'KSP_017***'\n")
    image_folder = select_folder()
    download_dir = f'{image_folder}/{shoot_id}'

    browser = webdriver.Chrome(options=setting_chrome_options())
    enable_download()

    shoot_link = autorization()  # авторизируюсь и получаю ссылку на данную съемку
    images_number = images_number_in_shot()  # int число с количеством снимков в съемке
    print(f'{images_number = }')
    main_cycle()
    time.sleep(15)
    browser.close()
    browser.quit()
    system_notification(f'Work completed for shoot {shoot_id}', f'{images_number} files downloaded to {download_dir}')
