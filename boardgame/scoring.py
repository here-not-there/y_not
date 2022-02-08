import random
import pprint

BOARD_SIZE = 10
EMPTY = 0
WHITE = 1
BLACK = 2
CELL_OPTIONS = [EMPTY, WHITE, BLACK]
LOOSE = 5
DIRECTIONS = [
    (-1, -1),  # Top left to bottom right
    (-1, 0),  # Top to bottom
    (-1, 1),  # Top right to bottom left
    (0, -1)   # Left to right
]

CURRENT = 1   # текущая строка счётчиков


def score(matrix):
    # читаем массив построчно
    # массив state хранит накопительные счётчики клеток одного цвета лежащих на прямых,
    # на которых находитс текущая клетка (вертикаль, горизонталь, две диагонали);
    # для работы достаточно двух state, один из которых - это результат для предыдущей строки

    # создаём список списков счётчиков для текущей и предыдущей строки
    state = [[[0] * len(DIRECTIONS) for _ in matrix[0]] for _ in range(2)]

    white_loose = False
    black_loose = False
    win_color = None

    for y, row in enumerate(matrix):
        # текущий счётчик становится бывшим
        state = state[::-1]
        for x, color in enumerate(row):
            cell = state[CURRENT][x]

            # опрашиваем все направления
            for dir_index, (y_diff, x_diff) in enumerate(DIRECTIONS):
                prev_x = x + x_diff

                # если клетка пуста, обнуляем результат для направления
                if color == EMPTY:
                    cell[dir_index] = 0
                # если не пуста, предыдущая клетка направления лежит на доске
                # и цвет в данном направлении совпадает - увеличиваем счётчик
                elif 0 <= prev_x < len(row) and color == matrix[y + y_diff][prev_x]:
                    cell[dir_index] = state[CURRENT +
                                            y_diff][prev_x][dir_index] + 1
                else:

                    # в остальных случаях начинаем считать заново
                    cell[dir_index] = 1

                if cell[dir_index] == LOOSE:
                    if color == WHITE:
                        white_loose = True
                        print('White loose')
                        win_color = WHITE
                    else:
                        black_loose = True
                        print('Black loose')
                        win_color = BLACK
    return win_color


