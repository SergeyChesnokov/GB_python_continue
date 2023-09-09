# ////////////////   Task #8   ////////////////
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from random import randint

friends = ['Иванов', 'Петров', 'Сидоров']
set_of_things = {'топор', 'спички', 'парафин', 'сухой спирт', 'нож', 'ружьё', 'термос', 'котелок', 'патроны', 'зажигалка',\
                 'фонарик', 'удочка', 'железная кружка', 'алюминевая ложка', 'GPS', 'рация', 'веревка', 'бутылка с водой'}

items_dict = {}
_set_of_taken = set()
while set_of_things != _set_of_taken:
    '''Заполняет словарь с
    ключем: имя друга,  и
    значением:  кортеж вещей,
    случайным набором из
    заданного множества вещей
    с возможными повторами.
    '''
    for friend in friends:
        thing = list(set_of_things) [randint(0,len(set_of_things) - 1)]
        # выбираем случайную вещь, а затем закидываем ее в кортеж
        # поочередно каждому другу до тех пор, пока не останется
        # неиспользованных вещей.
        if friend not in items_dict:
            items_dict.setdefault(friend, (thing, ))
        else:
            items_dict[friend] += (thing, )
        _set_of_taken.add(thing)


#  ===   Словарь items_dict   ===

for friend in items_dict:
    '''Делает вывод словаря более читаемым.
    '''
    print(f'\n{friend}:\n{items_dict[friend]}\n')


# 1. Какие вещи взяли все три друга
print('1. Какие вещи взяли все три друга')
_set_of_taken = set_of_things
for friend in items_dict:
    ''' Выводит только те вещи, которые взяли все друзья
    '''
    _set_of_taken = _set_of_taken & set(items_dict[friend])

print(f'{_set_of_taken} взяли все\n\n')


# 2. Какие вещи уникальны, есть только у одного друга 
print('2. Какие вещи уникальны, есть только у одного друга')
for friend in items_dict:
    
    a = set(items_dict[friend]) # переменная, для операций с удаленным элементом после его удаления
    b = list(items_dict[friend]) # переменная для возврата удаленного элемента
    items_dict[friend] = set()

    for _friend in items_dict:
        a -= set(items_dict[_friend])
    print(f'Только {friend} взял {a}' if a != set() else f'{friend} не уникален')
    items_dict[friend] = set(b)


# 3. Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
print('\n\n3. Кто остался без предмета')

for friend in items_dict:
    a = set()
    for _friend in items_dict:
        a |=  items_dict[_friend]
    a -= items_dict[friend]
    print(f'{friend} не взял {a}')
        
