from published_images import publication_info
from write_xlsx import write_to_file

red = '\033[91m'
green = '\33[32m'
end = '\033[0m'


def images_in_cycle(images_voc, path_to_file,check_date):
    count = 0
    print(images_voc)
    for k in images_voc:
        count += 1
        image_info = publication_info(k, count,check_date)
        write_to_file(path_to_file, image_info, count, check_date)

def one_day_images_cycle(images_voc,i):
    print(f"{red} in  {i} - {len(images_voc)} were send to publication{end}")
    print(f'{images_voc = }')
    count = 0
    for k in images_voc:
        count += 1
        image_info = publication_info(k, count,i)
        
images_voc = {'3265721': 'KSP_016797_00079', '3630967': 'KMO_189359_00044', '3631012': 'KMO_189359_00123', '3631017': 'KMO_189359_00049', '3631016': 'KMO_189359_00162', '3631018': 'KMO_189359_00065', '3630448': 'KSP_017660_00001'}

i = 'source_page_03.08.2022.html'
one_day_images_cycle(images_voc,i)



