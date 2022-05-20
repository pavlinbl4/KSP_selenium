from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from os import getenv


load_dotenv()
login = getenv('login')
password = getenv('password')
first_loggin = getenv('first_loggin')

shoot_id = 'KSP_015339'
image_folder = '/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency'
download_dir = f'/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/{shoot_id}'


def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    return chrome_options

def enable_download(browser):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)



browser = webdriver.Chrome(options=setting_chrome_options())
enable_download(browser)



def make_shoot_edit_link(link):
    shoot_edit_link = f'https://image.kommersant.ru/photo{link[2:]}'
    return shoot_edit_link


def get_image_links(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[9]
    tbody = table.find('tbody')
    images_links = tbody.find_all(title="Добавить кадрировку")
    return images_links
#
#
def go_my_images(page_link) -> object:
    browser.get(page_link)
    browser.save_screenshot(f'screen_short_{page_link[-3:]}.png')
    html = browser.page_source
    return html


def main_cycle(images_number, shoot_link):
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
        images_number = \
            browser.find_element(By.CSS_SELECTOR,
                                 'body > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > '
                                 'table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > '
                                 'td:nth-child(1) > b:nth-child(1)').text
    except:
        print('снимков с данным ключевым словом не найдено')
        images_number = 0
    images_number = int(images_number.replace(' ', ''))  # удаляю возможные пробелы перед преобразованием в целое число
    return images_number


def create_folder(shoot_id):
    os.makedirs(f'{image_folder}/{shoot_id}', exist_ok=True)


def autorization(shoot_id):  # авторизация гна главной странице
    create_folder(shoot_id)  # создаю папку для скачивания снимков
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#code').send_keys(shoot_id)  # ввожу номер съемки
    # browser.find_element(By.CSS_SELECTOR,'#lib0').click() # выбор только KP фото в данном случае не нужен
    select = Select(browser.find_element(By.NAME, 'ps'))
    select.select_by_value('100')
    browser.find_element(By.CSS_SELECTOR, '#searchbtn').click()
    browser.save_screenshot(f'{image_folder}/{shoot_id}/Screen_short_{shoot_id}.png')  # создаю скриншот для проверки
    shoot_link = browser.current_url[:-1]
    return shoot_link



shoot_link = autorization(shoot_id)  # авторизируюсь и получаю ссылку на данную съемку
images_number = images_number_in_shot()  # int число с количеством снимков в съемке
print(f'{images_number = }')
main_cycle(images_number, shoot_link)
time.sleep(15)
browser.close()
browser.quit()
