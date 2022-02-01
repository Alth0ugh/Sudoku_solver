from tkinter import *
from tkinter import ttk

class SudokuGrid():
    def __value_changed(self, value, coordinates):
        pass
    def __init__(self):
        root = Tk()

        root.geometry("500x500")

        for i in range(12):
            for j in range(12):
                if (j % 4 != 0 and i % 4 != 0):
                    sr = StringVar()
                    sr.trace("w", lambda name, index, mode, sr=sr: self.__value_changed(sr.get(), str(i) + str(j)))

                    frame = Frame(root, width = 40, height = 40)
                    text_box = Entry(frame, textvariable = sr)
                    frame.grid_propagate(False)
                    frame.columnconfigure(0, weight = 1)
                    frame.rowconfigure(0, weight = 1)
                    frame.configure(highlightbackground="black")
                    frame.configure(highlightthickness=1)

                    frame.grid(row = i, column = j)
                    text_box.grid(sticky = "wens")
                elif (j % 4 == 0):
                    separator = ttk.Separator(root, orient = "vertical")
                    separator.grid(row = i, column = j, sticky = "ns")
                elif (i % 4 == 0):
                    separator = ttk.Separator(root, orient = "horizontal")
                    separator.grid(row = i, column = j, sticky = "ns")
        root.mainloop()