# //////////////   Hometask #1   //////////////
# Напишите функцию для транспонирования матрицы


from random import randint

def matrix_random(n, m):
    '''Генерирует матрицу заданного размера из случайных чисел
    '''
    return [[randint(-15, 15) for _ in range (n)] for _ in range(m)]


def transposition(lst):
    '''Транспонирует матрицу
    '''
    return [[row[i] for row in lst] for i in range(len(lst[0]))]


def print_matrix(lst):
    '''Печать матрицы в традиционном виде
    '''
    indent = 8*len(lst[0])
    delimiter = '\n' + '='*indent + '\n'
    print(delimiter)
    for i in lst:
        for j in i:
            print(f'{j:4d}', end='\t')
        print('')
    print(delimiter)


# ===   Задаём размер матрицы ===
n,m = input('\nВведите количество столбцов (n = ) и строк (m = ) матрицы:   ').split()
n = int(n)
m = int(m)

# === Генерирует матрицу из случайных чисел ===
lst = matrix_random(n, m)
print_matrix(lst)

# === Транспонирует матрицу ===
lst = transposition(lst)
print_matrix(lst)

