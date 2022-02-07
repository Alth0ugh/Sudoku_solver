from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class SudokuGrid():
    def __value_changed(self, value, coordinates, variable):
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
        self.__squares = [None] * 81
        x = 0
        y = 0
        vars_iterator = 0
        for i in range(12):
            for j in range(12):
                if (j % 4 != 0 and i % 4 != 0):
                    sr = StringVar(name = str(x) + "_" + str(y))
                    sr.trace("w", lambda name, index, mode, sr=sr: self.__value_changed(sr.get(), sr._name, sr))
                    self.__vars[vars_iterator] = sr

                    frame = Frame(self.__root, width = 40, height = 40)
                    text_box = Entry(frame, textvariable = sr)
                    self.__squares[vars_iterator] = text_box
                    frame.grid_propagate(False)
                    frame.columnconfigure(0, weight = 1)
                    frame.rowconfigure(0, weight = 1)
                    frame.configure(highlightbackground="black")
                    frame.configure(highlightthickness=1)

                    frame.grid(row = i, column = j)
                    text_box.grid(sticky = "wens")

                    vars_iterator += 1

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
        return_val = [[-1 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                return_val[i][j] = self.__sudoku[i][j]
        return return_val

    def clear_sudoku(self):
        for i in range(81):
            self.__vars[i].set("")
            if (self.__squares[i].config()["state"][4] == "disabled"):
                self.__squares[i].configure(state = "normal")

    def show_answer(self, solved_sudoku):
        for i in range(9):
            for j in range(9):
                self.__vars[i * 9 + j].set(solved_sudoku[i][j])

    def lock_grid(self):
        for entry in self.__squares:
            if (entry.get() != ""):
                entry.configure(state = "disabled")
   