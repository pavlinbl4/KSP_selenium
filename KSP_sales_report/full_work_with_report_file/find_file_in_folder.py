import os
import re


def find_file(report_dir):  # возвращает пути к файлам отчета в Downloads
    all_file_paths = []
    list_of_files = os.listdir(report_dir)
    pattern = r'\AПавленко.+\.xls|Pavlenko.+\.xls'
    for file_name in list_of_files:
        if re.match(pattern, file_name):
            all_file_paths.append(f"{report_dir}/{file_name}")
    return all_file_paths
