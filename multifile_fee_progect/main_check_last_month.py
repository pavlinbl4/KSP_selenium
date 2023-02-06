"""
1. в фотоархивве можно отсмотреть только историю "засыла" изображений
2. "засланное" изображение не всегда опубликовано, нужно проверть это отдельно
"""
from kommersant_dates import KommersantDates
from published_images import autorization, select_today_published_images, end_selenium
from aditional_scripts.user_home_folder import home
from check_published_images import one_day_images_cycle
from cycle_for_html_save import month_cycle
from images_links import get_image_links
from images_vocabulary import make_images_voc
import re
import os
from pathlib import Path
from create_report_file import create_report_file

# 1. Нужны данные по предыдущему месяцу

kd = KommersantDates()  # вводя число получаю сдвиг с последнего дня месяца на указанное значение
check_date = kd.previous_month_check_day  # по умолчанию это последний день месяца
days_in_month = kd.days_in_month  # количество дней в месяце
path_to_file = create_report_file(kd.previous_month_name)

# 2. нужно пройтись по всем дням месяца и получить данные о "засланных" снимках

# 2.1 создаю папку для хранения html данных

html_folder = home.add_subfolder_to_kommersant(f'test_{kd.previous_month_name}/HTML')
# os.makedirs(html_folder,exist_ok=True)

# 2.2  авторизируюсь на сайте
autorization()

# 3 на данном этапе сохраню все страницы для последующего анализа
# for day in range(days_in_month,0,-1):
#     kd = KommersantDates(day)
#     check_date = kd.previous_month_check_day
#
#     html = select_today_published_images(check_date)
#
#     with open(f'{html_folder}/source_page_{check_date}.html', 'w') as file:
#         file.write(html)

# заменяю на функцию
# month_cycle(days_in_month, html_folder)

# end()

# 4 перебираю сохраненные страницы
count = 0 # счетчик опубликованнеых снимков за весь месяц
list_of_html = os.listdir(html_folder)
for i in list_of_html:
    with open(f'{html_folder}/{i}', 'r') as file:
        html = file.read()
    images_links = get_image_links(html)  # список ссылок на "засланные" снимки
    images_voc = make_images_voc(images_links)  # словарь из "внутреннего" id снимка и стандартного, внешного  id
    count = one_day_images_cycle(images_voc, re.findall(r'\d{2}.\d{2}.\d{4}',i)[0], path_to_file, count)
    print(f'{i} - {count}')


end_selenium()
