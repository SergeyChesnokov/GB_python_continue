# //////////////   Hometask #2   //////////////
# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь,

# где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте
# его строковое представление.


def formula_1(keys):
    dct = {}
    for i in keys:
        try:
            hash(i)            
        except:
            i = str(i) 
        dct.setdefault(i, hash(i))     
    return dct


_keys = [1,'one', [1], 1.0, (1), {1}, '', True, 1, None, 2, False, 0, True]

dct = formula_1(_keys)
print()
for key, value in dct.items():
    print(f'{key}:\t{value:>25}')

