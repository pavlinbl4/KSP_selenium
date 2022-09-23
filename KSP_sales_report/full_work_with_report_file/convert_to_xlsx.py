from xls2xlsx import XLS2XLSX
import os


def convert_to_xlsx(report_file):
    x2x = XLS2XLSX(report_file)
    x2x.to_xlsx(f"{report_file}x")
    os.remove(report_file)
    return f"{report_file}x"  # возвращаю путь к файлу с новым расширением
