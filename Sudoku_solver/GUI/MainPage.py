from tkinter import *
from GUI.SupervisedSolverPage import *

class MainPage():
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry("500x500")
        solver_page = SupervisedSolverPage(self.__root)
        self.__root.mainloop()