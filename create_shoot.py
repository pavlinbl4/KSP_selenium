""" недописанный скрипт для создания съемки в архиве
"""
from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import os
from os import getenv

login = getenv('login')
password = getenv('password')
first_loggin = getenv('first_loggin')

def system_notification(number, shoot_caption):
    title = "Съемка создана"
    message = f"Съемка {number}: {shoot_caption} созданна"
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


login = login
password = password
first_loggin = first_loggin

today_date = f'{datetime.now().strftime("%d.%m.%Y")}'

shoot_caption = input("Введите описание съемки\n")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
browser = webdriver.Chrome(options=options)

try:
    browser.get(first_loggin)
    login_input = browser.find_element(By.ID, "login")
    login_input.send_keys(login)

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)

    browser.find_element(By.CSS_SELECTOR, ".system input.but").click()
    author_input = browser.find_element(By.CSS_SELECTOR, "input#au")
    author_input.send_keys("Евгений Павленко")

    browser.find_element(By.CSS_SELECTOR,
                         "body > table.logotbl > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2) > a").click()
    browser.find_element(By.ID,
                         "nav_shoots_change").click()

    # добавляю описание съемки
    caption_input = browser.find_element(By.ID, "ShootDescription")
    caption_input.send_keys(shoot_caption)

    # ввожу дату
    day_input = browser.find_element(By.ID, "DateFrom")

    day_input.send_keys(today_date)

    time_input = browser.find_element(By.ID, 'TimeFrom')
    time_input.send_keys(Keys.NUMPAD1)

    time_input.send_keys(Keys.SPACE)

    time_input = browser.find_element(By.ID, 'TimeTo')
    time_input.send_keys(Keys.NUMPAD2)

    time_input.send_keys(Keys.SPACE)

    # выпадающее меню выбираю с помощью кнопок клавиатуры
    customer_input = browser.find_element(By.ID, "CustomerContact")
    customer_input.send_keys("Павленко Евгений Валентинович")
    time.sleep(1)
    customer_input.send_keys(Keys.DOWN)
    customer_input.send_keys(Keys.ENTER)



    # выбираю бильдредактора с помощью класса Select
    editor = browser.find_element(By.ID, 'EditorContactID')
    select = Select(browser.find_element(By.NAME,'EditorContactID'))
    select.select_by_value('2571')


    author_input = browser.find_element(By.ID, "AuthorContact")
    author_input.send_keys("Павленко Евгений Валентинович")
    time.sleep(1)
    author_input.send_keys(Keys.DOWN)
    time.sleep(1)
    author_input.send_keys(Keys.ENTER)
    time.sleep(1)

    browser.find_element(By.ID, 'SubmitBtn').click()

    number = browser.find_element(By.ID,"shootnum").text
    number = number.replace("№ ","KSP_0")
    pyperclip.copy(number)

    system_notification(number, shoot_caption)



    time.sleep(1)
    browser.close()
    browser.quit()
except Exception as ex:
    print(ex)
    browser.close()
    browser.quit()
