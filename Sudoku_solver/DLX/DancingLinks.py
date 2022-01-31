from DLX.Cell import *
from DLX.Header import *

class DancingLinks():
    def __init__(self):
        self.__found_solutions = [None] * 81
        self.__solution_count = 0
        self.__header = Header()
        self.__counter = 0

    def __construct_links(self, sudoku_matrix):
        header_iterator = self.__header
        header_iterator.name = "master"
        first_row = None
        first_column = None
        first_block = None
        first_square = None

        for i in range(9):
            for j in range(9):
                new_square = Header()
                new_square.name = str(i + 1) + str(j + 1)
                new_square.size = 0
                header_iterator.right = new_square
                new_square.left = header_iterator
                new_square.up = new_square
                new_square.down = new_square
                header_iterator = new_square
                if (i == 0 and j == 0):
                    first_square = new_square
        
        for i in range(9):
            for j in range(9):
                new_column = Header()
                new_column.name = str(i + 1) + "r" + str(j + 1)
                new_column.size = 0
                header_iterator.right = new_column
                new_column.left = header_iterator
                new_column.up = new_column
                new_column.down = new_column
                header_iterator = new_column
                if (i == 0 and j == 0):
                    first_row = new_column

        for i in range(9):
            for j in range(9):
                new_column = Header()
                new_column.name = str(i + 1) + "c" + str(j + 1)
                new_column.size = 0
                header_iterator.right = new_column
                new_column.left = header_iterator
                new_column.up = new_column
                new_column.down = new_column
                header_iterator = new_column
                if (i == 0 and j == 0):
                    first_column = new_column

        for i in range(9):
            for j in range(9):
                new_column = Header()
                new_column.name = str(i + 1) + "b" + str(j + 1)
                new_column.size = 0
                header_iterator.right = new_column
                new_column.left = header_iterator
                new_column.up = new_column
                new_column.down = new_column
                header_iterator = new_column
                if (i == 0 and j == 0):
                    first_block = new_column

        header_iterator.right = self.__header
        self.__header.left = header_iterator

        row_iterator = first_row
        column_iterator = first_column
        square_iterator = first_square
        previous_column_iterator = column_iterator
        block_iterator = first_block
        previous_block_iterator = block_iterator

        for i in range(81):
            for j in range(9):
                new_row_cell = Cell()
                new_column_cell = Cell()
                new_block_cell = Cell()
                new_square_cell = Cell()

                new_square_cell.left = new_block_cell
                new_square_cell.right = new_row_cell
                
                new_row_cell.left = new_square_cell
                new_row_cell.right = new_column_cell

                new_column_cell.left = new_row_cell
                new_column_cell.right = new_block_cell

                new_block_cell.left = new_column_cell
                new_block_cell.right = new_square_cell

                #Insert row cell
                new_row_cell.down = row_iterator.down
                row_iterator.down.up = new_row_cell
                row_iterator.down = new_row_cell

                new_row_cell.up = row_iterator
                new_row_cell.column = row_iterator
                row_iterator.size += 1

                #Insert column cell
                new_column_cell.down = column_iterator.down
                column_iterator.down.up  = new_column_cell
                column_iterator.down = new_column_cell

                new_column_cell.up = column_iterator
                new_column_cell.column = column_iterator
                column_iterator.size += 1

                #Insert block cell
                new_block_cell.down = block_iterator.down
                block_iterator.down.up = new_block_cell
                block_iterator.down = new_block_cell

                new_block_cell.up = block_iterator
                new_block_cell.column = block_iterator
                block_iterator.size += 1

                #Insert square cell
                new_square_cell.down = square_iterator.down
                square_iterator.down.up = new_square_cell
                square_iterator.down = new_square_cell

                new_square_cell.up = square_iterator
                new_square_cell.column = square_iterator
                square_iterator.size += 1
                
                square_iterator = square_iterator.right

                column_iterator = column_iterator.right

                if ((j + 1) % 3 == 0):
                    block_iterator = block_iterator.right
            
            if ((i + 1) % 3 == 0):
                    previous_block_iterator = block_iterator
            else:
                block_iterator = previous_block_iterator        
                    
            if ((i + 1) % 9 == 0):
                previous_column_iterator = column_iterator
                square_iterator = first_square
            else:
                column_iterator = previous_column_iterator

            row_iterator = row_iterator.right

        for i in range(9):
            for j in range(9):
                sqaure_iterator = first_square
                if (sudoku_matrix[i][j] != -1):
                    number = sudoku_matrix[i][j]
                    while(square_iterator.name != str(i + 1) + str(j + 1)):
                        square_iterator = square_iterator.right
                    cell_iterator = square_iterator.down
                    self.__cover(square_iterator)
                    while(square_iterator != cell_iterator):
                        if (cell_iterator.left.column.name[0:1] == str(number)):
                            self.__found_solutions[self.__solution_count] = cell_iterator
                            self.__solution_count += 1
                            row_iterator = cell_iterator.right
                            while(row_iterator != cell_iterator):
                                self.__cover(row_iterator.column)
                                row_iterator = row_iterator.right
                        cell_iterator = cell_iterator.down

        self.__search(self.__solution_count)

    def __cover(self, column):
        left_column = column.left
        right_column = column.right

        right_column.left = left_column
        left_column.right = right_column

        row_iterator = column.down
        while(row_iterator != column):
            iterator = row_iterator.right
            while(iterator != row_iterator):
                up_element = iterator.up
                down_element = iterator.down

                down_element.up = up_element
                up_element.down = down_element

                left_column = iterator.column.left
                right_column = iterator.column.right

                iterator.column.size -= 1

                iterator = iterator.right
            row_iterator = row_iterator.down

    def __uncover(self, column):
        left_column = column.left
        right_column = column.right

        left_column.right = column
        right_column.left = column

        row_iterator = column.up
        while (row_iterator != column):
            column_iterator = row_iterator.left
            while(column_iterator != row_iterator):
                up_element = column_iterator.up
                down_element = column_iterator.down

                up_element.down = column_iterator
                down_element.up = column_iterator

                left_column = column_iterator.column.left
                right_column = column_iterator.column.right
                
                column_iterator.column.size += 1

                column_iterator = column_iterator.left
            row_iterator = row_iterator.up

    def __print_answer(self):
        solution = [[-1 for i in range(9)] for j in range(9)]
        for i in range(81):
            if (self.__found_solutions[i] != None):
                coordinate_cell = None
                if (self.__found_solutions[i].column.name[1] == "r"):
                    coordinate_cell = self.__found_solutions[i].left
                elif(self.__found_solutions[i].column.name[1] == "c"):
                    coordinate_cell = self.__found_solutions[i].left.left
                elif (self.__found_solutions[i].column.name[1] == "b"):
                    coordinate_cell = self.__found_solutions[i].right
                else:
                    coordinate_cell = self.__found_solutions[i]
                solution[int(coordinate_cell.column.name[0:1]) - 1][int(coordinate_cell.column.name[1:2]) - 1] = coordinate_cell.right.column.name[0:1]
        print(*solution, sep = "\n")

    def __find_smallest_header(self):
        minimum = self.__header.right.size
        iterator = self.__header.right

        while (iterator != self.__header):
            if (iterator.size < minimum):
                minimum = iterator.size
            iterator = iterator.right
        iterator = self.__header.right
        while(iterator != self.__header):
            if (iterator.size == minimum):
                return iterator
            iterator = iterator.right

    def __search(self, k):
        if (self.__header.right == self.__header):
            self.__print_answer()
            return
        column = self.__find_smallest_header()
        self.__cover(column)
        row_iterator = column.down
        while(row_iterator != column):
            self.__found_solutions[k] = row_iterator
            column_iterator = row_iterator.right
            while(column_iterator != row_iterator):
                self.__cover(column_iterator.column)
                column_iterator = column_iterator.right
            self.__search(k+1)
            column_iterator = self.__found_solutions[k].left
            column = self.__found_solutions[k].column
            while (column_iterator != self.__found_solutions[k]):
                self.__uncover(column_iterator.column)
                column_iterator = column_iterator.left
            row_iterator = row_iterator.down
        self.__uncover(column)
        self.__counter += 1

    def Solve(self, sudoku_matrix):
        #self.__search()
        #return self.__found_solutions
        self.__construct_links(sudoku_matrix)
        print(str(self.__counter))