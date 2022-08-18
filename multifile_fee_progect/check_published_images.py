from published_images import publication_info
from kommersant_dates import KommersantDates
from write_xlsx import write_to_file


def images_in_cycle(images_voc, path_to_file):
    count = 0
    print(images_voc)
    for k in images_voc:
        count += 1
        image_info = publication_info(k, count)
        write_to_file(path_to_file, image_info, count, KommersantDates().yesterday)
