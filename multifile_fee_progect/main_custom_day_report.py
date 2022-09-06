from kommersant_dates import KommersantDates
from create_report_file import create_report_file
from published_images import autorization
from published_images import select_published_images, end
from images_links import get_image_links
from images_vocabulary import make_images_voc
from check_published_images import images_in_cycle


kd1 = KommersantDates()
month_name = kd1.previous_month_name
days_in_month = kd1.days_in_month
print(f'{month_name = } , {days_in_month = }')
autorization()

for day in range(1, 2): # cycle for every day in the month
    kd = KommersantDates(day)
    report_date = kd.previous_month_custom_day
    print(report_date)
    path_to_file = create_report_file(report_date)  # 1 create report file or make new sheet in existing
    html = select_published_images(report_date)  # 2 get html from page of published photos
    images_links = get_image_links(html)  # 3 get list of published images
    images_voc = make_images_voc(images_links)  # 4 create vocabulary internal_id:standart_
    # print(images_voc)
    # 5 in cycle check images in vocabulary and create report print it and write to xlsx  file
    images_in_cycle(images_voc, path_to_file, report_date)
# html = select_published_images(report_date)  # 2 get html from page of published photos
#
# images_links = get_image_links(html)  # 3 get list of published images
#
# images_voc = make_images_voc(images_links)  # 4 create vocabulary internal_id:standart_id



# 5 in cycle check images in vocabulary and create report print it and write to xlsx  file
# images_in_cycle(images_voc,path_to_file, report_date)

# end()




