"""
get real publication for the image KP archive
"""

from bs4 import BeautifulSoup

publication_page = '/Users/evgeniy/Desktop/test_page/Kommersant Photo Archive История публикаций_2.html'

with open(publication_page, 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

main_table = soup.find(id='Table1').find('tbody')

in_main_table_paper = main_table.find(class_="tblh3").find_all_previous('tr', class_=["myorg", "fororg"])

for i in in_main_table_paper:
    if i.find_all('td')[0].find('img') is not None:
        print(i.find_all('td')[1].text, i.find_all('td')[2].text)
print()

in_main_table_electron = main_table.find(class_="tblh3").find_next(class_="tblh3").find_all_previous('tr',class_='electron')

print(len(in_main_table_electron))
for i in in_main_table_electron:
    if i.find_all('td')[0].find('img') is not None and i.find_all('td')[0].find('img').get('src').split('/')[-1] != 'cancel.gif':
        print(i.find_all('td')[1].text, i.find_all('td')[2].text)
