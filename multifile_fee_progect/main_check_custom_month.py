"""
1. в фотоархивве можно отсмотреть только историю "засыла" изображений
2. "засланное" изображение не всегда опубликовано, нужно проверить это отдельно
"""
from kommersant_dates import KommersantDates
from published_images import autorization, end_selenium, select_today_published_images
from aditional_scripts.user_home_folder import home
from check_published_images import one_day_images_cycle
from images_links import get_image_links
from images_vocabulary import make_images_voc
import re
import os
from create_report_file import create_report_file
import calendar
from datetime import datetime
from calendar import monthrange

month_number = 6  # int(input('input months number'))

current_year = datetime.now().year
end_month = monthrange(current_year, month_number)[1]
months_name = calendar.month_name[month_number]
check_date = datetime(current_year, month_number, end_month).strftime("%d.%m.%Y")
days_in_month = end_month

path_to_file = create_report_file(months_name)

# 2. нужно пройтись по всем дням месяца и получить данные о "засланных" снимках

# 2.1 создаю папку для хранения html данных

html_folder = home.add_subfolder_to_kommersant(f'test_{months_name}/HTML')
os.makedirs(html_folder, exist_ok=True)

# 2.2  авторизируюсь на сайте
autorization()

# 3 на данном этапе сохраню все страницы для последующего анализа
for day in range(1, days_in_month + 1):
    check_date = datetime(current_year, month_number, day).strftime("%d.%m.%Y")

    html = select_today_published_images(check_date)

    with open(f'{html_folder}/source_page_{check_date}.html', 'w') as file:
        file.write(html)

# заменяю на функцию
# month_cycle(days_in_month, html_folder)

# end()

# 4 перебираю сохраненные страницы
# count = 0  # счетчик опубликованнеых снимков за весь месяц
# list_of_html = os.listdir(html_folder)
# for i in list_of_html:
#     with open(f'{html_folder}/{i}', 'r') as file:
#         html = file.read()
#     images_links = get_image_links(html)  # список ссылок на "засланные" снимки
#     images_voc = make_images_voc(images_links)  # словарь из "внутреннего" id снимка и стандартного, внешного  id
#     count = one_day_images_cycle(images_voc, re.findall(r'\d{2}.\d{2}.\d{4}', i)[0], path_to_file, count)
#     print(f'{i} - {count}')

end_selenium()
