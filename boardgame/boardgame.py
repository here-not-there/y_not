import random

import scoring as sc
import pprint
import copy

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

moves_list = []

nonhuman_side = None
human_side = None
winner = None

def select_color():
    global human_side
    global nonhuman_side
    while True:
        print('Choose side:\n White (input 1)\n Black (input 2)')
        color_input = input()
        if color_input == '1':
            human_side = sc.WHITE
            nonhuman_side = sc.BLACK
            break
        if color_input == '2':
            human_side = sc.BLACK
            nonhuman_side = sc.WHITE
            break


def human_moves(current_board):
    while True:
        print('Enter your move as x,y')
        move = input()
        try:
            x, y = move.split(',')
        except ValueError:
            continue
        x = int(x)
        y = int(y)
        if (x < 0) or (x > 9) or (y < 0) or (y > 9):
            print('Неверные координаты')
        elif (x, y) in moves_list:
            print('Такой ход уже был')
        else:
            break
    current_board[y][x] = human_side
    moves_list.append((x, y))


def computer_moves(current_board):
    test_board = copy.deepcopy(current_board)
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) in moves_list:
            continue
        test_board[y][x] = nonhuman_side
        moves_list.append((x, y))
        if (sc.score(board)) == human_side:
            test_board[y][x] = 0
            continue
        else:
            current_board[y][x] = nonhuman_side
            print('Ход компьютера : ', x, y)
            moves_list.append((x, y))
            break

select_color()
if nonhuman_side == sc.WHITE:
    computer_moves(board)
while True:
    human_moves(board)
    pprint.pprint(board)
    winner  = sc.score(board)
    if winner:
        print(winner)
        break
    computer_moves(board)
    pprint.pprint(board)
    winner  = sc.score(board)
    if winner:
        print(winner)
        break
