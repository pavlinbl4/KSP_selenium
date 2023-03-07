"""
in  publication_voc = scrap_publication_list() find publications in  check_date

"""

red = '\033[91m'
green = '\33[32m'
end = '\033[0m'


def checked_day_publications_only(check_date, publication_voc, count):
    image_info = {}
    for i in publication_voc:
        if publication_voc[i][0] == check_date:
            image_info['A'] = count
            image_info['B'] = publication_voc[0]
            image_info["C"] = publication_voc[i][0]
            image_info["D"] = publication_voc[i][1]
            image_info["E"] = publication_voc[i][2]
    return image_info


def checked_month_publications_only(check_date, publication_voc, count):
    image_info = {}
    for i in publication_voc:
        if publication_voc[i][1] == 'Соцсети (Коммерсантъ-Москва)' and publication_voc[i][3][3:] == check_date[3:]:
            image_info['A'] = count
            image_info['B'] = publication_voc[0]
            image_info['C'] = publication_voc[i][3]
            image_info["D"] = publication_voc[i][1]

        if publication_voc[i][0][3:] == check_date[3:]:
            image_info['A'] = count
            image_info['B'] = publication_voc[0]
            image_info["C"] = publication_voc[i][0]
            image_info["D"] = publication_voc[i][1]
            image_info["E"] = publication_voc[i][2]
    return image_info
