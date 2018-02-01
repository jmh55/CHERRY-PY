import calendar
import sys

def main():
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2018, 2, 0, 0)
    print(st)

if __name__ == "__main__":
    main()

