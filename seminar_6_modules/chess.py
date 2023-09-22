"""
"""


def checkmate(qw_pos: list) -> bool:
    qw_row = [i[0] for i in qw_pos] # сформирован список 1-х координат ферзей
    qw_col = [i[1] for i in qw_pos] # сформирован список 2-х координат ферзей
    qw_main_diag = [i[0] - i[1] for i in qw_pos]
    qw_scnd_diag = [i[0] + i[1] for i in qw_pos]
    for i in range(8):
        if any([
            qw_row.count(qw_row[i]) > 1,
            qw_col.count(qw_col[i]) > 1,
            qw_main_diag.count(qw_main_diag[i]) > 1,
            qw_scnd_diag.count(qw_scnd_diag[i]) > 1
        ]):
            return False
        else:
            return True
        

# qw_pos = [[0, 4], [1, 6], [2, 0], [3, 2], [4, 7], [5, 5], [6, 3], [7, 1]]


# qw_row = [i[0] for i in qw_pos] 
# qw_col = [i[1] for i in qw_pos]

# qw_main_diag = [i[0] - i[1] for i in qw_pos]
# qw_scnd_diag = [i[0] + i[1] for i in qw_pos]

# print(qw_main_diag)