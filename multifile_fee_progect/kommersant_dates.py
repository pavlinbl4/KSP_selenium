from datetime import datetime, timedelta


class KommersantDates:
    def __init__(self, day_cycle=1):
        today = datetime.today()
        self.today = today.strftime("%d.%m.%Y")
        self.previous_month_name = (today.replace(day=1) - timedelta(days=1)).strftime('%B')
        self.previous_month_last_day = (datetime.today().replace(day=1) - timedelta(days=day_cycle)).strftime(
            "%d.%m.%Y")
        self.days_in_month = int((datetime.today().replace(day=1) - timedelta(days=1)).strftime('%d'))
        self.yesterday = (today - timedelta(days=1)).strftime("%d.%m.%Y")
        self.previous_month_check_day = (datetime.today().replace(day=1) - timedelta(days=day_cycle)).strftime(
            "%d.%m.%Y")
