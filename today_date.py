from datetime import datetime

print(datetime.today())

print(datetime.today().day)

print(datetime.today().month)
print(datetime.today().strftime('%B'))
print(datetime.today().strftime('%Y_%B'))

print(datetime.today().year)

day = f"{str(datetime.today().day)}.{str(datetime.today().month)}.{datetime.today().year}"

print(day)
