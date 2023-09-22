''' Модуль проверки даты на существование.
'''

__all__ = ['date_checking_func']
MALTIPLE_OF_LEAP = 4
NOT_MALTIPLE_OF_LEAP = 100
MONTHS = 12
DAYS = 30
SHORT_MONTHS = 4, 6, 9, 11,


def _leap_year_checking_func(y: int) -> str:
    """ Проверяет год на високосность.
    Принимает на вход число - номер года,
    выводит строку, високосный это год или нет.
    """
    y_4 = y % MALTIPLE_OF_LEAP
    y_100 = y % NOT_MALTIPLE_OF_LEAP
    y_400 = y % (NOT_MALTIPLE_OF_LEAP*MALTIPLE_OF_LEAP)
    if (y_4 == 0) & (y_100 != 0) | (y_400 == 0):
        return 'leap year'
    else:
        return 'non-leap year'
    

def date_checking_func(date: list) -> str:
    """ Проверяет дату на соответствие календарю.
    Принимает на вход дату в формате DD.MM.YYYY,
    выводик строку, соответствует или нет.
    """
    d, m, y = date
    # создаём словарь существующих дат {месяц: количество дней}
    month_day_dict = {month: DAYS+1 for month in range(1, MONTHS+1)}    
    for month in SHORT_MONTHS:
        month_day_dict[month] = DAYS
    if _leap_year_checking_func(y) == 'leap year':
        month_day_dict[2] = DAYS - 1
    else:
        month_day_dict[2] = DAYS - 2
    # определяем есть ли дата в словаре существующих дат
    result = 'not'
    if m in range(1, MONTHS+1):
        if d in range(1, month_day_dict[m]):
            result = 'really'
            return f'Such a date does {result} exist'
    return f'Such a date does {result} exist'

if __name__ == '__main__':

    for date in (
        '01.01.2000'.split('.'), 
        '01.13.2000'.split('.'),
        '29.02.2023'.split('.'),
        '32.01.2000'.split('.'),
        ):
        for i in range(len(date)):
            date[i] = int(date[i])
        print(date_checking_func(date))






