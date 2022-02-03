from tkinter import *
from GUI.SudokuGrid import *
from DLX.DancingLinks import *

class SolverPage():
    def __init__(self, root):
        frame = Frame(root)
        button_frame = Frame(frame)
        solve_button = Button(button_frame, text = "Vyrieš", command = self.solve)
        clear_button = Button(button_frame, text = "Vymaž", command = self.clear_sudoku)
        self.__sudoku_grid = SudokuGrid(frame)
        self.__sudoku_grid.pack(side = LEFT)
        button_frame.pack(side = LEFT)
        solve_button.pack()
        clear_button.pack()
        frame.pack()

    def solve(self):
        current_sudoku = self.__sudoku_grid.get_sudoku()
        dancing_links = DancingLinks()
        solution = dancing_links.Solve(current_sudoku)
        if (solution == None):
            messagebox.showinfo("Chyba riešenia", "Nebolo možné nájsť žiadne riešenie zadaného sudoku.")
            return
        self.__sudoku_grid.show_answer(solution)

    def clear_sudoku(self):
        self.__sudoku_grid.clear_sudoku()