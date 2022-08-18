from selenium.webdriver.chrome.options import Options

def setting_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # фоновый режим
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    return chrome_options