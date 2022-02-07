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

        self.__hint_button = Button(button_frame, command = self.get_hint, text = "Nápoveda", state = "disabled")
        self.__hint_button.pack()

        self.__solve_button = Button(button_frame, command = self.solve_sudoku, text = "Skontroluj riešenie", state = "disabled")
        self.__solve_button.pack()

        self.__clear_button = Button(button_frame, command = self.clear, text = "Vymaž")
        self.__clear_button.pack()

        master_frame.pack()
        button_frame.pack(side = LEFT)
        
    def lock_grid(self):
        self.__sudoku_grid.lock_grid()
        self.__dancing_links = DancingLinks()

        self.__lock_button.configure(state = "disabled")
        self.__hint_button.configure(state = "normal")
        self.__solve_button.configure(state = "normal")

    def get_hint(self):
        messagebox.showinfo("Nápoveda", self.__dancing_links.get_hint(self.__sudoku_grid.get_sudoku()))

    def solve_sudoku(self):
        solved_sudoku = self.__dancing_links.Solve(self.__sudoku_grid.get_sudoku())
        if (solved_sudoku == None):
            messagebox.showinfo("Výsledok kontroly", "Vaše riešenie nie je správne")
        else:
            messagebox.showinfo("Výsledok kontroly", "Vaše riešenie alebo priebežné riešenie je správne")

    def clear(self):
        self.__lock_button.configure(state = "normal")
        self.__hint_button.configure(state = "disabled")
        self.__solve_button.configure(state = "disabled")
        self.__sudoku_grid.clear_sudoku()