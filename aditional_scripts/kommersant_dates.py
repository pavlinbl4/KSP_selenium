from datetime import datetime, timedelta


class KommersantDates:
    def __init__(self):
        today = datetime.today()
        self.today = today.strftime("%d.%m.%Y")
        self.previous_month_name = (today.replace(day=1) - timedelta(days=1)).strftime('%B')
        self.previous_month_last_day = (datetime.today().replace(day=1) - timedelta(days=1))
        self.days_in_month = int((datetime.today().replace(day=1) - timedelta(days=1)).strftime('%d'))


# kd = KommersantDates()
#
# print(kd.previous_month_name)