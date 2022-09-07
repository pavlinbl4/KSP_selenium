"""
get real publication for the image KP archive
"""

from bs4 import BeautifulSoup


def image_publications_voc(report_html):
    soup = BeautifulSoup(report_html, 'lxml')

    main_table = soup.find(id='Table1').find('tbody')

    def main_table_paper_only():
        return main_table.find(class_="tblsubhead").find_all_next('tr', class_=["myorg", "fororg"])

    def main_table_electron_only():
        return main_table.find(class_="tblsubhead").find_all_next('tr', class_='electron')

    def main_table_paper_other():
        return main_table.find(class_="tblh3").find_all_previous('tr', class_=["myorg", "fororg"])

    def main_table_electron_other():
        return main_table.find(class_="tblh3").find_next(class_="tblh3") \
            .find_all_previous('tr', class_='electron')


    if main_table.find(class_="tblh3") is None:  # no table "другие фотографии этой съемки" on the page
        main_table_paper = main_table_paper_only()
        main_table_electron = main_table_electron_only()

    elif main_table.find(class_="tblh3") is not None and main_table.find(class_="tblh3").find_next(class_="tblh3") is not None:
        main_table_paper = main_table_paper_other()
        main_table_electron = main_table_electron_other()

    elif main_table.find(class_="tblh3") is not None and main_table.find(class_="tblh3").find_next(class_="tblh3") is None:
        main_table_paper = main_table_paper_other
        main_table_electron = main_table_electron_only()

    elif main_table.find(class_="tblh3") is None and main_table.find(class_="tblh3").find_next(
            class_="tblh3") is not None:
        main_table_paper = main_table_paper_only()
        main_table_electron = main_table_electron_other()

    work_tables = [main_table_paper, main_table_electron]

    publication_voc = {}
    publication_voc[0] = soup.find('h3').text[16:].strip()
    count = 1
    for table in work_tables:  # make same operation for two different tables
        for i in table:

            pub_check = i.find('td',class_='center').find('img')
            if len(i) == 9:
                shift = 1
            elif len(i) == 8:
                shift = 0
            if pub_check is not None:
                if pub_check.get('src').split('/')[-1] == 'yes.gif':
                    publication_date = i.find_all('td')[1 + shift].text[:10]
                    publication_place = i.find_all('td')[2 + shift].text.strip()
                    material = i.find_all('td')[4 + shift].text.strip()
                    publication_voc[count] = [publication_date, publication_place, material]
                    count += 1
    return publication_voc


# test

# offline_html = '/Users/evgeniy/Desktop/test_page/Kommersant Photo Archive История публикаций.html'
# with open(offline_html, 'r') as file:  # read offline  html page
#     report_html = file.read()
# image_publications_voc(report_html)
# for _ in image_publications_voc(report_html).items():
#     print(_)