import pandas as pd


def get_itog_from_file(input_file):  # получаю цифру итога из отчета и преобразую ее в число
    itog_digit = pd.read_excel(input_file)
    itog_sum = \
        itog_digit[itog_digit['Unnamed: 1'] == 'Итого автору причитается вознаграждение в размере:'][
            'Unnamed: 14'].values[
            0]
    itog_sum = float(
        itog_sum.strip().replace(' руб.', '').replace(',', '.').replace(' ', ''))  # преобразую в числовое значение
    return itog_sum


def check_external_sales_spelling(df):
    if len(df[df.client == "Внешняя реализация"]) == 0:
        return df[df.client == "внешняя реализация"]
    return df[df.client == "Внешняя реализация"]


def dataframe_from_xlsx(input_file):
    df = pd.read_excel(input_file, sheet_name=0, skiprows=10)  # считываю данные пропуская шапку отчета
    df = df.rename(columns={'Издание, №, дата публикации': 'client',
                            'Полоса': 'page',
                            'Название': 'name',
                            'Внутренний код фотоизображения': 'image_id',
                            'Авторское вознаграждение, руб': 'income'}) \
        [['client', 'name', 'image_id', 'income']]
    return df.dropna(how='all')  # удаляю строки полностью из Nan


def convert_report_to_csv(report_file):
    # считывание данных по публикациям и базовая обработка датафрэйма
    df = dataframe_from_xlsx(report_file)
    month_name = pd.read_excel(report_file, sheet_name=0, nrows=1, skiprows=2).dropna(axis=1)['Unnamed: 9'][0][17:]

    # нахожу индекс строки "внешняя реализация"
    test_df = check_external_sales_spelling(df)
    external_sales_id = test_df.index.values.astype(int)[
        0]  # индекс cтроки с надписю "Внешняя реализация"
    external_sales_amount = test_df['income'].values.astype(float)[
        0]  # сумма внешних продаж из отчета

    # создаю датафрэйм для внешних продаж ( в старых отчетах он будет пустым)
    external_sales_df = df.loc[external_sales_id + 1:]
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

    itog_sum_from_file = get_itog_from_file(report_file)  # итоговая сумма из файла отчета

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
        return df_optimization, external_sales_df, kommersant_sales_df, month_name
    else:
        print(
            f" \033[31m ошибка в расчете \n - итог по отчету {itog_sum_from_file} \n"
            f" - рассчитанный итог {itog_sum_calculated}\n"
            f"")
