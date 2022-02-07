from tkinter import *
from GUI.SolverPage import *
from GUI.SupervisedSolverPage import *

class MainPage():
    def __init__(self):
        self.__root = Tk()
        self.setup_main_page()

    def go_back(self):
        for child in self.__root.winfo_children():
            child.destroy()
        self.setup_main_page()

    def setup_main_page(self):
        self.__root.geometry("500x500")
        
        self.__back_button_frame = Frame(self.__root)

        back_button = Button(self.__back_button_frame, text = "<-", command = self.go_back)
        back_button.pack(side = LEFT)

        self.__back_button_frame.pack(fill = X)

        self.__menu_frame = Frame(self.__root)
        
        self.__supervised_button = Button(self.__menu_frame, text = "Sudoku Helper", command = self.show_supervised_solver_page)
        self.__supervised_button.pack()

        self.__solver_button = Button(self.__menu_frame, text = "Sudoku Solver", command = self.show_solver_page)
        self.__solver_button.pack()

        self.__menu_frame.pack()

        self.__root.mainloop()

    def show_solver_page(self):
        for child in self.__root.winfo_children():
            child.destroy()

        self.__back_button_frame = Frame(self.__root)

        back_button = Button(self.__back_button_frame, text = "<-", command = self.go_back)
        back_button.pack(side = LEFT)

        self.__back_button_frame.pack(fill = X)

        solver_page = SolverPage(self.__root)

    def show_supervised_solver_page(self):
        for child in self.__root.winfo_children():
            child.destroy()

        self.__back_button_frame = Frame(self.__root)

        back_button = Button(self.__back_button_frame, text = "<-", command = self.go_back)
        back_button.pack(side = LEFT)

        self.__back_button_frame.pack(fill = X)

        supervised_solver = SupervisedSolverPage(self.__root)