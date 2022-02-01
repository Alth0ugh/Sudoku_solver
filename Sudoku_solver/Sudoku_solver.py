from DLX.DancingLinks import *
from GUI.SolverPage import *

#sudoku_matrix = [
#    [4,-1,3,-1,2,-1,7,-1,8],
#    [-1,2,-1,4,-1,8,-1,3,-1],
#    [7,-1,8,-1,1,-1,4,-1,2],
#    [-1,7,-1,3,-1,1,-1,2,-1],
#    [9,-1,2,-1,5,-1,8,-1,3],
#    [-1,3,-1,2,-1,9,-1,4,-1],
#    [3,8,7,1,4,2,5,9,6],
#    [6,4,9,8,3,5,2,7,1],
#    [2,5,1,6,9,7,3,8,4]
#    ]

#8022 backtracks, easy
#sudoku_matrix = [
#    [-1,1,-1,9,-1,6,7,-1,-1],
#    [5,-1,-1,-1,-1,-1,1,-1,-1],
#    [7,-1,8,5,-1,-1,-1,-1,2],
#    [8,-1,4,-1,-1,1,-1,-1,-1],
#    [-1,6,-1,-1,-1,-1,-1,1,-1],
#    [-1,-1,-1,2,-1,-1,6,-1,7],
#    [3,-1,-1,-1,-1,2,5,-1,6],
#    [-1,-1,9,-1,-1,-1,-1,-1,1],
#    [-1,-1,1,6,-1,7,-1,8,-1]
#    ]

#10389 backtracks, hard
#sudoku_matrix = [
#    [6,9,-1,-1,7,2,-1,-1,1],
#    [-1,-1,-1,-1,5,-1,2,-1,-1],
#    [-1,-1,-1,4,-1,-1,-1,-1,-1],
#    [1,-1,-1,7,3,-1,6,-1,-1],
#    [5,-1,6,-1,-1,-1,7,-1,3],
#    [-1,-1,8,-1,4,6,-1,-1,9],
#    [-1,-1,-1,-1,-1,3,-1,-1,-1],
#    [-1,-1,1,-1,6,-1,-1,-1,-1],
#    [9,-1,-1,8,1,-1,-1,5,6]
#    ]

sudoku_matrix = [
    [-1,2,-1,5,-1,-1,4,-1,-1],
    [-1,-1,3,9,-1,1,-1,-1,-1],
    [-1,6,-1,7,2,-1,-1,-1,-1],
    [6,-1,-1,-1,1,-1,2,-1,-1],
    [5,-1,-1,-1,-1,-1,-1,-1,3],
    [-1,-1,1,-1,5,-1,-1,-1,8],
    [-1,-1,-1,-1,8,3,-1,1,-1],
    [-1,-1,-1,6,-1,9,7,-1,-1],
    [-1,-1,9,-1,-1,5,-1,6,-1]
    ]

main_menu = SudokuGrid()