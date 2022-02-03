from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class SudokuGrid():
    def __value_changed(self, value, coordinates):
        coord = coordinates.split("_")
        if (value.isnumeric()):
            self.__sudoku[int(coord[0])][int(coord[1])] = int(value)
        elif(value.isnumeric() == False and value != ""):
             messagebox.showinfo("Chyba", "Zadali ste text namiesto čísla")
             variable.set("")
        elif (value == ""):
            self.__sudoku[int(coord[0])][int(coord[1])] = -1

    def __init__(self, master):
        self.__root = Frame(master)
        self.__vars = [None] * 81
        x = 0
        y = 0
        vars_iterator = 0
        for i in range(12):
            for j in range(12):
                if (j % 4 != 0 and i % 4 != 0):
                    sr = StringVar(name = str(x) + "_" + str(y))
                    sr.trace("w", lambda name, index, mode, sr=sr: self.__value_changed(sr.get(), sr._name))
                    self.__vars[vars_iterator] = sr
                    vars_iterator += 1

                    frame = Frame(self.__root, width = 40, height = 40)
                    text_box = Entry(frame, textvariable = sr)
                    frame.grid_propagate(False)
                    frame.columnconfigure(0, weight = 1)
                    frame.rowconfigure(0, weight = 1)
                    frame.configure(highlightbackground="black")
                    frame.configure(highlightthickness=1)

                    frame.grid(row = i, column = j)
                    text_box.grid(sticky = "wens")

                    y += 1
                    if (y > 8):
                        x += 1
                        y = 0
                elif (j % 4 == 0):
                    separator = ttk.Separator(self.__root, orient = "vertical")
                    separator.grid(row = i, column = j, sticky = "ns")
                elif (i % 4 == 0):
                    separator = ttk.Separator(self.__root, orient = "horizontal")
                    separator.grid(row = i, column = j, sticky = "ns")
        self.__sudoku = [[-1 for i in range(9)] for j in range(9)]

    def grid(self, row, column):
        self.__root.grid(row = row, column = column)

    def pack(self, side):
        self.__root.pack(side = side)

    def get_sudoku(self):
        return self.__sudoku

    def clear_sudoku(self):
        for var in self.__vars:
            var.set("")

    def show_answer(self, solved_sudoku):
        for i in range(9):
            for j in range(9):
                self.__vars[i * 9 + j].set(solved_sudoku[i][j])

