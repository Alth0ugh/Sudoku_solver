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
        counter = 0
        for i in range(9):
            for j in range(9):
                if (current_sudoku[i][j] != -1):
                    counter += 1
        if (counter < 17):
            messagebox.showinfo("Chyba", "Bolo zadaných príliš málo hodnôt. Zadajte sudoku, ktoré má aspoň 17 hodnôt.")
            return

        dancing_links = DancingLinks()
        solution = dancing_links.Solve(current_sudoku)
        if (solution == None):
            messagebox.showinfo("Chyba riešenia", "Nebolo možné nájsť žiadne riešenie zadaného sudoku.")
            return
        self.__sudoku_grid.show_answer(solution)
        if (dancing_links.get_solution_count() > 1):
            messagebox.showinfo("Riešenie sudoku", "Sudoku má viac ako 1 riešenie. Zobrazujem jedno z nich.")

    def clear_sudoku(self):
        self.__sudoku_grid.clear_sudoku()