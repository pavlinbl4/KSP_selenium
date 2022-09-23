import os
import shutil


def move_file(report_file, year, destination, report_dir):  # переименовываю и перемещаю файл отчета

    file_name = os.path.basename(report_file)

    os.makedirs(f"{destination}/{year}", exist_ok=True)
    working_file = f"{destination}/{year}/{file_name}"
    print(f'working_file = {working_file}')
    if os.path.exists(working_file):  # надо вставить проверку на случай если файл отчета уже есть
        os.remove(report_file)
        print('данный отчет уже обработан ранее')
        return
    file_to_work = shutil.move(f"{report_dir}/{file_name}", working_file)
    print(f"обработан файл - {file_to_work}")  # главная переменная с которой дальше буду работать
    return file_to_work
