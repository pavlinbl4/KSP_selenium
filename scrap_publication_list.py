"""
get real publication for the image KP archive
"""

from bs4 import BeautifulSoup

publication_page = '/Users/evgeniy/Documents/Kommersant/Kommersant Photo Archive История публикаций.html'

with open(publication_page, 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

main_table = soup.find(id='Table1').find('tbody')

main_table_paper = main_table.find(class_="tblh3").find_all_previous('tr', class_=["myorg", "fororg"])
main_table_electron = main_table.find(class_="tblh3").find_next(class_="tblh3")\
    .find_all_previous('tr',class_='electron')

work_tables = [main_table_paper,main_table_electron]


publication_voc = {}
count = 1
for table in work_tables: # make same operation for two different tables
    for i in table:
        # print(i.find_all('td')[0].find('img'))
        pub_check = i.find_all('td')[0].find('img')
        if pub_check is not None:
            if pub_check.get('src').split('/')[-1] == 'yes.gif':
                publication_date = i.find_all('td')[1].text[:10]
                publication_place = i.find_all('td')[2].text.strip()
                material = i.find_all('td')[4].text.strip()
                publication_voc[count] = [publication_date,publication_place, material]
                count += 1
    print()





# for i in main_table_electron:
#     if i.find_all('td')[0].find('img') is not None and i.find_all('td')[0].find('img').get('src').split('/')[-1] != 'cancel.gif':
#         publication_date = i.find_all('td')[1].text[:10]
#         publication_place = i.find_all('td')[2].text.strip()
#         material = i.find_all('td')[4].text.strip()
#         publication_voc[publication_date] = [publication_place, material]

for _ in publication_voc.items():
    print(_)
