import matplotlib as plt
import numpy as np
from tkinter import *


def print_board(B):  # prints the board
    for i in range(len(B)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(B[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(B[i][j])
            else:
                print(str(B[i][j]) + " ", end="")


def find_empty(B):  # returns the index of first empty cell
    for row in range(9):
        for col in range(9):
            if int(B[row][col]) == 0:
                return row, col


def valid(B, num, pos):

    # checks element horizontally
    for j in range(9):
        if B[pos[0]][j] == num and pos[1] != j:
            return False

    # checks element vertically
    for i in range(9):
        if B[i][pos[1]] == num and pos[0] != i:
            return False

    # check inside 3x3box
    box_x = pos[0]//3
    box_y = pos[1]//3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if B[i][j] == num and pos != (i, j):
                return False

    return True


def solve(B):
    empty_cell = find_empty(B)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if valid(B, i, (row, col)):
            B[row][col] = i

            if solve(B):
                return True

            B[row][col] = 0
    return False


def main():

    # 7, 8, 0, 4, 0, 0, 1, 2, 0, 6, 0, 0, 0, 7, 5, 0, 0, 9, 0, 0, 0, 6, 0, 1, 0, 7, 8, 0, 0, 7, 0, 4, 0, 2, 6, 0, 0, 0, 1, 0, 5, 0, 9, 3, 0, 9, 0, 4, 0, 6, 0, 0, 0, 5, 0, 7, 0, 3, 0, 0, 0, 1, 2, 1, 2, 0, 0, 0, 7, 4, 0, 0, 0, 4, 9, 2, 0, 6, 0, 0, 7
    entries = list(map(int, input().split(",")))
    board = np.array(entries).reshape(9, 9)

    # print(board)

    draw(board)

    solve(board)

    draw(board)


def draw(board):
    frame = Tk()
    for i in range(9):
        for j in range(9):
            if (i in (0, 1, 2, 6, 7, 8) and j in (3, 4, 5) or
                    (i in (3, 4, 5) and j in (0, 1, 2, 6, 7, 8))):
                color = "light green"
            else:
                color = "white"

            if board[i][j] == 0:
                colorTxt = "red"
            else:
                colorTxt = "black"
            btn = Button(frame, height=3, width=6, state=DISABLED, disabledforeground=colorTxt,
                         text=board[i][j], bg=color,)
            btn.grid(row=i, column=j, sticky=N+S+E+W)

    mainloop()


if __name__ == "__main__":
    main()
