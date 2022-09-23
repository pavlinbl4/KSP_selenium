import pandas as pd


def get_date_from_xlsx(input_file):  # из шапки отчета получаю данные о дате периода отчета
    date = pd.read_excel(input_file, sheet_name=0, nrows=1, skiprows=2) \
        .dropna(axis=1)['Unnamed: 1'].values[0]
    x = date.replace('г.', '').split('.')
    year = x[2].strip()
    month_digit = x[1]
    return year, month_digit
