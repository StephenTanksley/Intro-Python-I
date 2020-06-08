from sys import argv
import calendar
from datetime import datetime

current_date = datetime.today()

print(current_date)


def show_calendar(day=current_date.day, month=current_date.month, year=current_date.year):
    cal = calendar.month(year, month)
    print(cal)


def exercise():
    try:
        if len(argv) == 3:
            show_calendar(month=int(argv[1]), year=int(argv[2]))
        elif len(argv) == 2:
            show_calendar(month=int(argv[1]))
        else:
            show_calendar()
    except ValueError:
        print(
            "Please input month and year using integers as command line arguments. e.g. 14_cal.py [month] [year].")
    except IndexError:
        print("Please provide a value of 1-12 in integers for the month.")


exercise()
