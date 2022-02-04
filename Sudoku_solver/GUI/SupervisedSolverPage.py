from tkinter import *
from tkinter import ttk
from GUI.SudokuGrid import *
from DLX.DancingLinks import *

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
        self.__sudoku_grid.lock_grid()
        self.__dancing_links = DancingLinks()
        self.__dancing_links.set_current_state(self.__sudoku_grid.get_sudoku())

    def get_hint(self):
        self.__dancing_links.modify_changes(self.__sudoku_grid.get_sudoku())
        messagebox.showinfo("Nápoveda", self.__dancing_links.get_hint())

    def solve_sudoku(self):
        pass