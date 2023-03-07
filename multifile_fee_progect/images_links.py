from bs4 import BeautifulSoup


def get_image_links(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all('table')[9].find('tbody').find_all(title="Добавить кадрировку")
