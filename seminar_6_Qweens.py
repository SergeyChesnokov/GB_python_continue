# ///////////////////   Задача о 8 ферзях  ///////////////////

from random import sample
from seminar_6_modules import chess

FIELD_SIZE = 8
QWEENS = 8

#  - случайная расстановка
# field = [[i, j] for i in range(FIELD_SIZE) for j in range(FIELD_SIZE)] # создаём пустое поле
# qw_pos = [field[i] for i in sample(range(64), 8)] # расставляем ферзей (qweens)

#  - ручная расстановка ферзей
qw_pos = [[0, 4], [1, 6], [2, 0], [3, 2], [4, 7], [5, 5], [6, 3], [7, 1]]

print(qw_pos)

print(chess.checkmate(qw_pos))
