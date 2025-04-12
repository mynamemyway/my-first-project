year = 2025

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True


def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        return 30
    elif month_index == 1:
        return 29 if is_leap_year(year_value) else 28
    else:
        return 31


def print_days(days_in_month, start_day):
    print('    ' * start_day, end='')  # 4 пробела на день
    for day in range(1, days_in_month + 1):
        print(f'{day:2}', end='  ')  # выравнивание по ширине
        if (day + start_day) % 7 == 0:
            print()
    if (days_in_month + start_day) % 7 != 0:
        print()


def print_header(year_value, month_index):
    print(f'\n{months[month_index]} {year_value}')
    print('Пн  Вт  Ср  Чт  Пт  Сб  Вс')


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
    print(f'\nКалендарь на {year} год\n{"=" * 25}')

    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)
        print_days(duration, start_day)
        start_day = adjust_start_day(start_day, duration)
        print('-' * 28)
    print('creator: mynamemyway')


print_calendar(year)
