"""
главный файл для обработки отчета из Коммерсанта
преобразование отчета коммерсанта в
CSV файл с необходимой информацией
протестирован июнь 2022
но скрипт работает если имя файла написанно на латинице
"""

import pandas as pd
import os
from xls2xlsx import XLS2XLSX
import fnmatch
import shutil

report_dir = '/Volumes/big4photo/Downloads'
destination = '/Volumes/big4photo/Documents/Kommersant/Reports_files/original_reports'


def move_file(input_file, report_dir, destination):  # переименовываю и перемещаю файл отчета
    year, month_digit = get_date_from_xlsx(input_file)
    file_name = os.path.basename(input_file)

    os.makedirs(f"{destination}/{year}", exist_ok=True)
    working_file = f"{destination}/{year}/{file_name}"
    print(f'working_file = {working_file}')
    if os.path.exists(
            working_file):  # надо вставить проверку на случай если файл отчета уже есть. то прекратить работу. удалив исходник
        os.remove(input_file)
        print('данный отчет уже обработан ранее')
        return
    file_to_work = shutil.move(f"{report_dir}/{file_name}", working_file)
    print(f"обработан файл - {file_to_work}")  # главная переменная с которой дальше буду работать


def convert_to_xlsx(report_dir):
    list_of_files = os.listdir(report_dir)
    pattern = 'Pavlenko_*.xls'
    count = 0
    for file_name in list_of_files:
        if fnmatch.fnmatch(file_name, pattern):
            count += 1
            x2x = XLS2XLSX(f"{report_dir}/{file_name}")
            x2x.to_xlsx(f"{report_dir}/{file_name.capitalize()}x")
            os.remove(f"{report_dir}/{file_name}")
    # print(f"Сконвертированно {count} файлов")
    return count


def find_report(report_dir, destination):  # поск заданных файлов в папке загрузок создаем input_file
    list_of_files = os.listdir(report_dir)
    pattern = 'Pavlenko_evgen*.xlsx'
    count = 0
    for file_name in list_of_files:
        if fnmatch.fnmatch(file_name, pattern):
            count += 1
            # action with file
            print(f'\033[39m выполняю действие с файлом {file_name}')
            input_file = f'{report_dir}/{file_name}'
            # 3 сконвертированный файл найден преобразую его в csv
            convert_report_to_csv(input_file)
            # 5 перемещаю обработанный файл в архивную папку - выполняю операцию в функциии записи данных

    return input_file

    if count == 0:
        print('нет нужного файла')


def get_date_from_xlsx(input_file):
    date = pd.read_excel(input_file, sheet_name=0, nrows=1, skiprows=2) \
        .dropna(axis=1)['Unnamed: 1'].values[0]
    x = date.replace('г.', '').split('.')
    year = x[2].strip()
    month_digit = x[1]
    return year, month_digit


def get_itog_from_file(input_file):  # получаю цифру итога из отчета и преобразую ее в число
    itog_digit = pd.read_excel(input_file)
    itog_sum = \
        itog_digit[itog_digit['Unnamed: 1'] == 'Итого автору причитается вознаграждение в размере:'][
            'Unnamed: 14'].values[
            0]
    itog_sum = float(
        itog_sum.strip().replace(' руб.', '').replace(',', '.').replace(' ', ''))  # преобразую в числовое значение
    return itog_sum


def write_to_csv(df_optimization, month_name, external_sales_df, kommersant_sales_df, input_file):
    year, month_digit = get_date_from_xlsx(input_file)
    os.makedirs(
        f"/Volumes/big4photo/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}",
        exist_ok=True)

    df_optimization.to_csv(
        f"/Volumes/big4photo/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/optimization_report_2021_{month_name}.csv", index=False)
    external_sales_df.to_csv(
        f"/Volumes/big4photo/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/only_external_sales_report_2021_{month_name}.csv",
        index=False)
    kommersant_sales_df.to_csv(
        f"/Volumes/big4photo/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/kommersant_sales_report_2021_{month_name}.csv",
        index=False)


def dataframe_from_xlsx(input_file):
    df = pd.read_excel(input_file, sheet_name=0, skiprows=10)
    df = df.rename(columns={'Издание, №, дата публикации': 'client', \
                            'Полоса': 'page', \
                            'Название': 'name', \
                            'Внутренний код фотоизображения': 'image_id', \
                            'Авторское вознаграждение, руб': 'income'}) \
        [['client', 'name', 'image_id', 'income']]
    return df.dropna(how='all')  # удаляю строки полностью из Nan


def check_externak_sales_spelling(df):
    if len(df[df.client == "Внешняя реализация"]) == 0:
        return df[df.client == "внешняя реализация"]
    return df[df.client == "Внешняя реализация"]


def convert_report_to_csv(input_file):
    month_name = pd.read_excel(input_file, sheet_name=0, nrows=1, skiprows=2) \
                     .dropna(axis=1)['Unnamed: 9'][0][17:]  # месяц отчета

    # считывание данных и базовая обработка датафрэйма
    df = dataframe_from_xlsx(input_file)

    # нахожу индекс строки "внешняя реализация"
    test_df = check_externak_sales_spelling(df)
    external_sales_id = test_df.index.values.astype(int)[
        0]  # индекс cтроки с надписю "Внешняя реализация"
    external_sales_amount = test_df['income'].values.astype(float)[
        0]  # сумма внешних продаж из отчета

    # создаю датафрэйм для внешних продаж ( в старых отчетах он будет пустым)
    external_sales_df = df.loc[external_sales_id + 1:]
    # external_sales_df = external_sales_df.dropna(subset=["image_id"])  #  в декабрьском отчете у одной продажи нет id что приводит к ошибке
    external_sales_calculated = external_sales_df['income'].sum()
    print(f'external_sales_calculated - {external_sales_calculated}')

    # если нет  подробного отчета по внешним продажам, то использую итоговые данные из отчета
    if len(external_sales_df) == 0:
        external_sales_calculated = external_sales_amount

    # создаю датафрэйм для публикаций в коммерсанте
    kommersant_sales_df = df.loc[:external_sales_id]
    kommersant_sales_df = kommersant_sales_df.dropna(
        subset=["image_id"])  # публикации в печатных изданиях коммерсанта
    kommersant_sales_calculated = kommersant_sales_df['income'].sum()
    print(f'kommersant_sales_calculated - {kommersant_sales_calculated}')

    # создаю датафрэйм для публикаций в интернете
    internet_sales_df = df[df['client'] == 'Интернет издания']  # только интернет публикации во всех коммерсантах
    internet_sales_calculated = internet_sales_df['income'].sum()
    print(f'internet_sales_calculated = {internet_sales_calculated}')

    itog_sum_from_file = get_itog_from_file(input_file)  # итоговая сумма из файла отчета

    itog_sum_calculated = (
            kommersant_sales_calculated + external_sales_calculated + internet_sales_calculated).round(2)

    if itog_sum_from_file == itog_sum_calculated:
        print(f"Рассчет произведен правильно,"
              f"\n итог -  {itog_sum_calculated}"
              f"\n внешние продажи - {external_sales_amount.round(2)}"
              f"\n гонорары Ъ - {kommersant_sales_df['income'].sum().round(2)}"
              f"\n интернет публикации Ъ - {internet_sales_df['income'].sum().round(2)}")

        df_internet = df.groupby(['client'], as_index=False) \
            .sum() \
            .query('client == "Интернет издания"')
        df_sales = df.query('client == "Внешняя реализация"')
        df_image_id = df.dropna(subset=["image_id"])  # удаляю строки где нет данных про код фото
        df_optimization = df_image_id.append(df_internet)
        df_optimization.loc['Итог'] = df_optimization.sum(numeric_only=True, axis=0)
        df_optimization = df_optimization.append(df_sales)
        # 4 преобразование данных завершено записываю их в файл
        write_to_csv(df_optimization, month_name, external_sales_df, kommersant_sales_df,
                     input_file)  # записываю данные в файл
        # 5 перемещаю файл в архив
        move_file(input_file, report_dir, destination)

    else:
        print(
            f" \033[31m ошибка в расчете \n - итог по отчету {itog_sum_from_file} \n - рассчитанный итог {itog_sum_calculated}\n"
            f"")


def main():
    # 1 конвертирую скачанные файлы в папке downloads если их нет останавливаю скрипт
    if convert_to_xlsx(report_dir) != 0:
        print("файлы сконвертированны продолжаем работу")
        find_report(report_dir, destination)
        # перехожу к функции поиска нужных файлов в директории и обрабатываю их
    else:
        print("нечего конвертировать")
        find_report(report_dir, destination)
        #  2 ищу  сконвертированные файлы - это в итоге должно быть под if


main()
