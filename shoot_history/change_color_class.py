import pyexiv2
import os
from colorama import Fore


def change_color_class(file, image_title):
    changes = {}
    with open(file, 'rb+') as image_file:
        try:
            with pyexiv2.ImageData(image_file.read()) as meta_data:
                # data = meta_data.read_xmp()
                # changes['Xmp.photomechanic.ColorClass'] = 2
                # changes['Xmp.photoshop.Urgency'] = 2
                # changes['Xmp.dc.rights'] = {'lang="x-default"': 'pavlinbl4'}
                # changes['Xmp.photoshop.Credit'] = 0
                changes['Xmp.dc.creator'] = ['Eugene Pavlenko']
                changes['Xmp.xmp.Label'] = "Red"
                changes['Xmp.dc.title'] = {'lang="x-default"': image_title}
                # changes['Xmp.dc.description'] = {'lang="x-default"': "CAPTION"}
                # changes['Xmp.dc.subject'] = ['KEYWORD',"keywords"]
                meta_data.modify_xmp(changes)
                image_file.seek(0)
                image_file.truncate()
                image_file.write(meta_data.get_bytes())
            image_file.seek(0)
        except Exception as ex:
            print(f'{Fore.RED}{ex}{Fore.RESET}in file {Fore.GREEN}{os.path.basename(file)}{Fore.RED}')




file = "/Users/evgeniy/Pictures/2022/20220829_намывные территории/20220829EPAV0420.DNG"
image_title = 'test'
change_color_class(file, image_title)
