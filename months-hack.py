from datetime import datetime
import calendar
from collections import namedtuple

# Weekdays: Monday -> 0, ..., Sunday -> 6
if __name__ == '__main__':
    PersianMonth = namedtuple('PersianMonth', ['month_name', 'days_cnt', 'start_weekday'])
    days_cnt2month = {
        31:1, # January
        30:4, # April
        29:2  # February on leap years
    }
    persian_months = []
    persian_months.append(PersianMonth('Farvardin', 31, 1))
    persian_months.append(PersianMonth('Ordibehesht', 31, 4))
    persian_months.append(PersianMonth('Khordad', 31, 0))
    persian_months.append(PersianMonth('Tir', 31, 3))
    persian_months.append(PersianMonth('Mordad', 31, 6))
    persian_months.append(PersianMonth('Shahrivar', 31, 2))
    persian_months.append(PersianMonth('Mehr', 30, 5))
    persian_months.append(PersianMonth('Aban', 30, 0))
    persian_months.append(PersianMonth('Azar', 30, 2))
    persian_months.append(PersianMonth('Dey', 30, 4))
    persian_months.append(PersianMonth('Bahman', 30, 6))
    persian_months.append(PersianMonth('Esfand', 29, 1))

    for month in persian_months:
        for y in reversed(range(1, 2017)):
            dt = datetime(y, days_cnt2month[month[1]], 1)
            if dt.weekday() == month[2]:
                if month[1] == 29 and not calendar.isleap(y):
                    continue
                print('{} -> {}-{:02}-01'.format(month[0], y, days_cnt2month[month[1]]))
                break
