from bs4 import BeautifulSoup

p_page = '/Users/evgeniy/Documents/Kommersant/My_report_from_0107\source_page.html'

with open(p_page, 'r') as file:
    read_html = file.read()

soup = BeautifulSoup(read_html, 'lxml')
all_publications = soup.find(id='Table1').find('tbody').find_all('tr')
electron_pub = soup.find(class_="tblh3")
print(electron_pub)
# for i in electron_pub:
#     print(i.text)
# print(electron_pub.find_all_next())
print("find all next class='electron' after class='tblh3' ")
for i in electron_pub.find_all_next(class_="electron"):
    print(i)
