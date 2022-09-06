from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

DOWNLOAD_URL = "https://github.com/chandrashekhargoka/python_samples/archive/master.zip"
download_dir = "/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/"


def enable_download(browser):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return chrome_options


def is_file_downloaded():
    file_path = download_dir + "python_samples-master.zip"
    while not os.path.exists(file_path):
        time.sleep(1)
    if os.path.isfile(file_path):
        print("File Downloaded successfully..")


if __name__ == '__main__':
    browser = webdriver.Chrome(options=setting_chrome_options())
    enable_download(browser)
    browser.get(DOWNLOAD_URL)
    is_file_downloaded()
