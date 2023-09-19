# 1 - Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

from os import path


def path_tuple(path_: str) -> tuple:
    lst = path_.split('\\')
    path_ = ''
    for i in lst[:-1]:
        bs_ = '/'
        path_ = path_.__add__(i+bs_)
    name_, extension_ = lst[-1].split('.')

    return path_, name_, extension_,

path_ = path.abspath(__file__)
print('\n', path_tuple(path_), '\n')

