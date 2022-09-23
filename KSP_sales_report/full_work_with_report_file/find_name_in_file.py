import re


def find_my_name_in_file(file_name):  # return True or False
    pattern = r'\AПавленко.+\.xls|Pavlenko.+\.xls'
    return re.match(pattern, file_name)
