# from datetime import datetime, timedelta
from multifile_fee_progect.kommersant_dates import KommersantDates

kd = KommersantDates()

print(kd.previous_month_name)
print(kd.previous_month_last_day)
print(kd.days_in_month, type(kd.days_in_month))