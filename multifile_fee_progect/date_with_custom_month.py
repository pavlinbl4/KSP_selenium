import calendar
from datetime import datetime
from calendar import monthrange


def custom_month_date(month_number):
    current_year = datetime.now().year
    end_month = monthrange(current_year, month_number)[1]
    months_name = calendar.month_name[month_number]
    check_date = datetime(current_year, month_number, end_month).strftime("%d.%m.%Y")

    return months_name, check_date, end_month, current_year


