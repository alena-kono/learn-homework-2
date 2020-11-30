import datetime

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""


def print_days():
    timedeltas = {
        0: 'today',
        1: 'yesterday',
        30: '30 days ago'
        }
    for delta, message in timedeltas.items():
        print(
            f'{message.capitalize(): <12}:',
            f'{datetime.date.today() - datetime.timedelta(days=delta)}'
            )


def str_2_datetime(date_string):
    return datetime.datetime.strptime(
        date_string,
        '%d/%m/%y %H:%M:%S.%f'
        )


if __name__ == "__main__":
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))
