from datetime import datetime, timedelta


class KommersantDates:
    def __init__(self, cycle_day = 1):
        today = datetime.today()
        self.today = today.strftime("%d.%m.%Y")
        self.previous_month_name = (today.replace(day=1) - timedelta(days=1)).strftime('%B')
        self.previous_month_last_day = (datetime.today().replace(day=1) - timedelta(days=1)).strftime("%d.%m.%Y")
        self.days_in_month = int((datetime.today().replace(day=1) - timedelta(days=1)).strftime('%d'))
        self.yesterday = (today - timedelta(days=1)).strftime("%d.%m.%Y")
        shift_day = self.days_in_month - cycle_day + 1
        self.previous_month_custom_day = (datetime.today().replace(day=1) - timedelta(days=shift_day)).strftime("%d.%m.%Y")

# kd = KommersantDates()
# # # #
# # # print(kd.previous_month_name, kd.days_in_month)
# print(kd.previous_month_custom_day)
