from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# Ввод года
while True:
    try:
        year = int(input("Введите год (например, 2030): "))
        if year < 1:
            print("Пожалуйста, введите положительное число.")
            continue
        break
    except ValueError:
        print("Это не похоже на число. Попробуйте ещё раз.")

today = datetime.today()
is_current_year = (year == today.year)


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True


def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        return 30
    elif month_index == 1:
        return 29 if is_leap_year(year_value) else 28
    return 31


def print_days(days_in_month, start_day, current_day=None, current_month=None):
    print('   ' * start_day, end='')

    for day in range(1, days_in_month + 1):
        weekday = (start_day + day - 1) % 7
        is_today = (day == current_day and current_month)

        # Цвет дня
        color = ''
        if is_today:
            color = Fore.MAGENTA + Style.BRIGHT  # Изменено на BRIGHT для жирного шрифта
        elif weekday in [5, 6]:  # Суббота и Воскресенье
            color = Fore.WHITE + Style.DIM

        # Вывод числа
        if day < 10:
            print(f"{color} {day} ", end='')
        else:
            print(f"{color}{day} ", end='')

        if (day + start_day) % 7 == 0:
            print()

    if (days_in_month + start_day) % 7 != 0:
        print()


def print_header(year_value, month_index):
    # Добавляем разделительную линию перед каждым месяцем (кроме первого)
    if month_index > 0:
        print("\n" + "-" * 20)
    print(f"\n{Style.BRIGHT}{months[month_index]} {year_value}")
    print('Пн Вт Ср Чт Пт Сб Вс')


def get_starting_day(year):
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7


def adjust_start_day(start_day, days_in_month):
    return (start_day + days_in_month) % 7


def print_calendar(year):
    start_day = get_starting_day(year)

    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)

        current_day = today.day if is_current_year and month_number == today.month - 1 else None
        current_month = is_current_year and month_number == today.month - 1

        print_days(duration, start_day, current_day, current_month)
        start_day = adjust_start_day(start_day, duration)

    print("\ncreator: mynamemyway")


print_calendar(year)