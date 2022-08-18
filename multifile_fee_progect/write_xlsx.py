from openpyxl import load_workbook


def write_to_file(path_to_file, image_info, line_number, report_date):
    wb = load_workbook(path_to_file)
    ws = wb[report_date]
    ws[f'A{line_number + 2}'] = image_info['A']
    ws[f'B{line_number + 2}'] = image_info['B']
    ws[f'C{line_number + 2}'] = image_info['C']
    ws[f'D{line_number + 2}'] = image_info['D']
    ws[f'E{line_number + 2}'] = image_info['E']

    wb.save(path_to_file)