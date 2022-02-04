from tkinter import *
from tkinter import ttk
from GUI.SudokuGrid import *

class SupervisedSolverPage():
    def __init__(self, root):
        master_frame = ttk.Frame(root)
        self.__sudoku_grid = SudokuGrid(master_frame)
        self.__sudoku_grid.pack(side = LEFT)
        
        button_frame = ttk.Frame(master_frame)
        self.__lock_button = Button(button_frame, command = self.lock_grid, text = "Začni hrať")
        self.__lock_button.pack(side = TOP)

        self.__hint_button = Button(button_frame, command = self.get_hint, text = "Nápoveda")
        self.__hint_button.pack()

        self.__solve_button = Button(button_frame, command = self.solve_sudoku, text = "Skontroluj riešenie")
        self.__solve_button.pack()

        master_frame.pack()
        button_frame.pack(side = LEFT)

        
    def lock_grid(self):
        pass

    def get_hint(self):
        pass

    def solve_sudoku(self):
        pass