"""
наконеч то написан итоговый скрипт, который из файла отчета скачивает превью изображений внешних
продаж, генерирует упрощенные файлы в CSV и переносит скачанный файл отчета в нужную директорию
нужно только скачать файл отчета в Downloads и запустить скрипт
"""
from pathlib import Path
from colorama import Fore
import os
from get_reports_dates import get_date_from_xlsx
from csv_work import convert_report_to_csv
from find_file_in_folder import find_file
from convert_to_xlsx import convert_to_xlsx
from write_data_to_file import write_to_csv
from move_report_files import move_file
from get_external_prevue import download_prevue_external_sales

report_dir = f'{Path().home()}/Downloads'
os.makedirs(f'{Path().home()}/Documents/Kommersant/Reports_files/original_reports', exist_ok=True)
destination = f'{Path().home()}/Documents/Kommersant/Reports_files/original_reports'

# 1 check_downloads folder for report files
all_file_paths = find_file(report_dir)  # список путей к файлам отчета в Downloads

# 1.1 print report for find files
if len(all_file_paths) != 0:
    for i in all_file_paths:
        print(f"найден файл отчета - {Fore.RED}{os.path.basename(i)}{Fore.RESET}")
        # 2 конвертирую файлы в и создаю отдельные файлы отчетов в формате csv
        for report_file in all_file_paths:
            report_file = convert_to_xlsx(
                report_file)  # конвертирую в нужный для Pandas формат - временно экранирую но работает и без него
            year, month_digit = get_date_from_xlsx(report_file)  # дата отчета
            print(year, month_digit)
            df_optimization, external_sales_df, kommersant_sales_df, month_name = convert_report_to_csv(report_file)
            write_to_csv(df_optimization, month_name, external_sales_df, kommersant_sales_df, year,
                         month_digit)  # записываю упрощенные файлы отчетов в формате CSV

            file_to_work = move_file(report_file, year, month_digit, destination)  # путь к перемещенному файлу отчета

            download_prevue_external_sales(year, month_digit, month_name)

else:
    print(f"{Fore.RED}файлов отчета в старом формате не найдено {Fore.RESET}")
