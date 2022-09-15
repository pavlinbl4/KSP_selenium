import os
import re


def find_no_ext(file_name, path):  # this will match a file_name
    rg_pattern = r'[^.]+(?=\.)'
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            name_no_ext = re.findall(rg_pattern, name)
            if len(name_no_ext) != 0:
                if name_no_ext[0] == file_name:
                    result.append(os.path.join(root, name))
    return result
