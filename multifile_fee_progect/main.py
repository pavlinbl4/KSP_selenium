from kommersant_dates import KommersantDates
from create_report_file import create_report_file
from published_images import select_today_published_images, end
from images_links import get_image_links
from images_vocabulary import make_images_voc
from check_published_images import images_in_cycle


# create class element for kommersant days
kd = KommersantDates()

path_to_file = create_report_file(kd.yesterday)  # 1 create report file or make new sheet in existing

html = select_today_published_images()  # 2 get html from page of published photos

images_links = get_image_links(html)  # 3 get list of published images

images_voc = make_images_voc(images_links)  # 4 create vocabulary internal_id:standart_id



# 5 in cycle check images in vocabulary and create report print it and write to xlsx  file
images_in_cycle(images_voc,path_to_file)

end()




