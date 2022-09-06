"""
скрипт выводящий информацию о всех публикациях
за весь период нахождения снимка в архиве
по id снимка
"""

from published_images import select_today_published_images, end_selenium, autorization, check_id_image
from images_links import get_image_links
from images_vocabulary import make_images_voc
from check_published_images import image_id_cycle

image_id = 'KSP_016797_00019_1'


# нужно войти на сайт и получить данные по данному снимку

autorization()
html = check_id_image(image_id)
images_links = get_image_links(html)  # список ссылок на "засланные" снимки
images_voc = make_images_voc(images_links)   # словарь с внутренним id снимка и внешним id

rezult = image_id_cycle(images_voc)

for i in rezult:
    print(rezult[i])






end_selenium()