"""
get real publication for the image KP archive
"""

from bs4 import BeautifulSoup

red = '\033[91m'
green = '\33[32m'
end = '\033[0m'


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

    elif main_table.find(class_="tblh3") is not None and main_table.find(class_="tblh3").find_next(
            class_="tblh3") is not None:
        main_table_paper = main_table_paper_other()
        main_table_electron = main_table_electron_other()

    elif main_table.find(class_="tblh3") is not None and main_table.find(class_="tblh3").find_next(
            class_="tblh3") is None:
        main_table_paper = main_table_paper_other()
        main_table_electron = main_table_electron_only()

    elif main_table.find(class_="tblh3") is None and main_table.find(class_="tblh3").find_next(
            class_="tblh3") is not None:
        main_table_paper = main_table_paper_only()
        main_table_electron = main_table_electron_other()
    work_tables = [main_table_paper, main_table_electron]

    publication_voc = {0: soup.find('h3').text[16:].strip()}
    count = 1
    for table in work_tables:  # make same operation for two different tables
        for i in table:

            pub_check = i.find('td', class_='center').find('img')
            shift = 0
            if len(i) == 9:
                shift = 1

            if pub_check is not None:
                if pub_check.get('src').split('/')[-1] == 'yes.gif':
                    publication_date = i.find_all('td')[1 + shift].text[:10]
                    publication_place = i.find_all('td')[2 + shift].text.strip()
                    send_date = i.find_all('td')[7 + shift].text.strip()[:10]  # дата засыла снимка
                    # print(f"{i.find_all('td')[7 + shift].text.strip() = }")
                    material = i.find_all('td')[4 + shift].text.strip()
                    publication_voc[count] = [publication_date, publication_place, material, send_date]
                    count += 1
    return publication_voc
