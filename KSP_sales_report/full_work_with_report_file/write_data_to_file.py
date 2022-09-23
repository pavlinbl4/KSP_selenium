import os
from pathlib import Path

home = Path().home()


def write_to_csv(df_optimization, month_name, external_sales_df, kommersant_sales_df, year, month_digit):
    # year, month_digit = get_date_from_xlsx(input_file)
    os.makedirs(
        f"{home}/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}",
        exist_ok=True)

    df_optimization.to_csv(
        f"{home}/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/optimization_report_{year}_{month_name}.csv", index=False)
    external_sales_df.to_csv(
        f"{home}/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/only_external_sales_report_{year}_{month_name}.csv",
        index=False)
    kommersant_sales_df.to_csv(
        f"{home}/Documents/Kommersant/Reports_files/report_in_CSV/{year}/{month_digit}_{month_name}"
        f"/kommersant_sales_report_{year}_{month_name}.csv",
        index=False)
