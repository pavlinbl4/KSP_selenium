from published_images import publication_info, published_for_all_time
from write_xlsx import write_to_file, write_xlsx_single_sheet


red = '\033[91m'
green = '\33[32m'
end = '\033[0m'


def images_in_cycle(images_voc, path_to_file, check_date):
    count = 0
    print(images_voc)
    for k in images_voc:
        count += 1
        image_info = publication_info(k, count, check_date)
        write_to_file(path_to_file, image_info, count, check_date)


def one_day_images_cycle(images_voc, i, path_to_file, count):  # # проверяю каждый снимок из "засланных"
    print(f"{red} in  {i} - {len(images_voc)} were send to publication{end}")
    for k in images_voc:  # k - внутренний id снимка
        count += 1
        used_images = publication_info(k, count, i)  # получаю словарь с данными о всех публикациях данного снимка
        write_xlsx_single_sheet(path_to_file, used_images)  # записываю данную информацию в файл отчета
    return count


def image_id_cycle(images_voc):
    count = 0
    for k in images_voc:  # на самом деле снимок один и цикл не нужен - переделать
        count += 1
        image_info = published_for_all_time(k)
    return image_info
