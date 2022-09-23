from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from crome_options import setting_chrome_options
import csv
import time

home = Path().home()
browser = webdriver.Chrome(options=setting_chrome_options())


def autorization():  # авторизация на главной странице
    load_dotenv()
    login = getenv('login')
    password = getenv('password')
    first_loggin = getenv('first_loggin')
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    browser.find_element(By.CSS_SELECTOR, '#au').send_keys('Евгений Павленко')


def download_prevue_external_sales(year, month_digit, month_name):
    # работать будем с csv файлом отчета о внешних продажах, нужно сгенерить его путь
    csv_file_path = f'{home}/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}/only_external_sales_report_{year}_{month_name}.csv'

    autorization()

    prevue_folder = f"{home}/Documents/Kommersant/External_sales/{year}_внешние продажи"
    os.makedirs(f"{prevue_folder}/{month_name}", exist_ok=True)

    with open(csv_file_path, newline='') as csv_file:
        count = 0
        reader = csv.DictReader(csv_file)
        for row in reader:
            count += 1
            if row['image_id'].startswith("K"):
                new_window = browser.window_handles[0]  # необходимый модуль, браузер фокусируется на нужной вкладке
                browser.switch_to.window(new_window)

                shoot_input = browser.find_element(By.CSS_SELECTOR, "input#code")
                shoot_input.clear()
                shoot_input.send_keys(row['image_id'])
                browser.find_element(By.CSS_SELECTOR, ".note .but#searchbtn").click()
                # надо открыть окно с превью
                browser.find_element(By.CSS_SELECTOR, 'a[href^= "ViewPhoto"] .imgb').click()
                # переключаюсь на новое окно и скачиваю снимок
                new_window = browser.window_handles[1]
                browser.switch_to.window(new_window)
                time.sleep(2)
                # делаю скриншот, как скачать файл не разобрался

                browser.find_element(By.CSS_SELECTOR, ".imgb") \
                    .screenshot(
                    f"{prevue_folder}/{month_name}/{count}__{row['image_id']} - {row['income']}.png")
                browser.close()
    browser.quit()


