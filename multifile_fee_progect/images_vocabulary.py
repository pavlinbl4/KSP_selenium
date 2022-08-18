import re


def make_images_voc(images_links):
    images_voc = {}
    for i in images_links:
        ksp_id = re.findall(r'(?<=photocode=)\w{16}', str(i))[0]
        regex = r'(?<=photoid=)\d{7}(?=\")'
        photoid = re.findall(regex, str(i))[0]
        images_voc[photoid] = ksp_id
    return images_voc
