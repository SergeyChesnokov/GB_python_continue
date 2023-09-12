# //////////////   Hometask #3   //////////////
# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def refill(x):
    '''
    ПОПОЛНЕНИЕ СЧЕТА (ВНЕСЕНИЕ НА СЧЁТ)
    '''
    print(REFILL_MENU_TEXT)
    y = int(input('\nСколько купюр Вы ВНОСИТЕ?   '))
    transaction = y*NOTE
    global refill_list
    refill_list.append(transaction)
    x += transaction
    print(f'\nВы внесли {transaction:_.2f} у.е.\t {BALANCE_TEXT} {x:_.2f} у.е.')
    return x


def refill_report():
    '''ОТЧЕТ О ПОСТУПЛЕНИЯХ.
    '''
    print(REFILL_REPORT_TEXT)
    if refill_list != []:
        print
        for i in enumerate(refill_list):
            print(f'{i[0]}\t{i[1]:>{5*INDENT}}')
    else:
        print('Поступлений не было...')

def withdraw(x):
    '''
    СНЯТИЕ СО СЧЁТА
    '''
    print(WHITHDRAWAL_MENU_TEXT)
    y = int(input('\nСколько купюр Вы СНИМАЕТЕ?   '))
    transaction = y*NOTE

    # Вычисление комиссии
    fee = round(transaction*WITHDRAWAL_FEE, 2)   
    if fee < MIN_FEE:
        fee = MIN_FEE
    elif fee > MAX_FEE:
        fee = MAX_FEE

    # Проверка на доступный остаток
    global acc_balance
    if transaction + fee > acc_balance:
        print(LACK_TEXT)
        return x

    # Танзакция 
    x -= transaction + fee
    print('\nВы сняли', f'{transaction:_.2f}', 'у.е.\t', 'Комиссия', fee,'у.е.\t', BALANCE_TEXT, f'{x:_.2f}', 'у.е.')
    return x


def tax():
    '''
    УДЕРЖАНИЕ НАЛОГА НА БОГАТСТВО
    '''
    global acc_balance
    if acc_balance > WEALTH:
        print('-'*delimiter_2)
        print(f'\t{TAX_STR}\t{acc_balance*TAX:_.2f} у.е.')
        print('-'*delimiter_2)
        acc_balance -= acc_balance*TAX


# Константы
NOTE = 50
WITHDRAWAL_FEE = 1.5/100
MIN_FEE = 30
MAX_FEE = 600
INTERST = 3/100
TAX = 10/100
WEALTH = 5_000_000      

# Переменные
acc_balance = 0
refill_list = []

# Форматирование
INDENT = 5
BALANCE_TEXT = 'Остаток на счете: '
MAIN_MENU_TEXT_p1 = f'\n\n\t---<   Основное меню   >---\n\n\
        {BALANCE_TEXT}\t'
MAIN_MENU_TEXT_p2 = 'у.е.\n\n\
\
                1 - Пополнить\n\
                2 - Снять\n\
                3 - История поступлений\n\
                0 - Выйти\n'
REFILL_MENU_TEXT = f'\n\n\t---<   Пополнение счета   >---\n\n\
Возможно внесение только купюр по {NOTE} у.е.'
REFILL_REPORT_TEXT = f'\n\n\t---<   Отчет о поступлениях   >---\n\n'
WHITHDRAWAL_MENU_TEXT = f'\n\n\t---<   Снятие со счета   >---\n\n\
Возможно снятие только купюр по {NOTE} у.е.'
LACK_STR = '[X]   Недостаточно средств!!!   [X]'
delimiter_1 = len(LACK_STR) + 2*INDENT
LACK_TEXT = '\n\n' + '-'*delimiter_1 + '\n' + INDENT*' ' + LACK_STR + '\n' + '-'*delimiter_1
TAX_STR = 'УДЕРЖАН НАЛОГ НА БОГАТСТВО!!!'
delimiter_2 = len(TAX_STR) + 6*INDENT


# Основной код
while True:
    counter = 3
    while counter > 0:
        print(f'{MAIN_MENU_TEXT_p1} {acc_balance:_.2f} {MAIN_MENU_TEXT_p2}')
        n = int(input('Выберите действие:   '))
        if n == 1:
            # Вызов функции ПОПОЛНЕНИЯ refill()
            tax()
            acc_balance = refill(acc_balance)
            counter -= 1
        elif n == 2:
            # Вызов функции СНЯТИЯ withdraw()
            tax()
            acc_balance = withdraw(acc_balance)
            counter -= 1
        elif n == 3:
            # Вызов функции отчета о поступлениях refill_report
            refill_report()
        elif n == 0:
            # Завершение работы
            print('\nСпасибо за Ваш визит. До свиданья\n\n')
            exit()
        else:
            # Возврат в Основное меню
            print('Некорректный ввод!!!')
    else:
        # Начисление процентов каждые 3 операции при обнулении счетчика counter
        acc_balance += acc_balance*INTERST
        print('\nПоздравляем! Вам начислены проценты: ', acc_balance*INTERST, 'у.е.', BALANCE_TEXT, acc_balance, 'у.е.\n')
        continue

