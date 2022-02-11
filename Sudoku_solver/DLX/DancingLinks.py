from DLX.Cell import *
from DLX.Header import *

class DancingLinks():
    def __init__(self):
        self.__found_solutions = [None] * 81
        self.__solution_count = 0
        self.__header = Header()
        self.__header.name = "master"
        self.__solution = None
        self.__original_sudoku = None
        self.__answer_count = 0

    #Generates constraint table according to sudoku from the input.
    def __construct_links(self, sudoku_matrix):
        self.__solution = None
        self.__found_solutions = [None] * 81
        self.__solution_count = 0
        self.__answer_count = 0
        self.__header = Header()
        self.__header.name = "master"
        first_row = Header()
        first_column = Header()
        first_block = Header()
        first_square = Header()

        last_row = first_row
        last_column = first_column
        last_block = first_block
        last_square = first_square

        for i in range(9):
            for j in range(9):
                #Square column generation
                new_square = Header()
                #First digit is row index and the second digit is column index (both counting from 1).
                new_square.name = str(i + 1) + str(j + 1)
                new_square.size = 0
                new_square.up = new_square
                new_square.down = new_square
                new_square.left = last_square
                last_square.right = new_square
                last_square = new_square

                #Row column generation
                new_row = Header()
                #First digit is a number that is possible to insert into the row and the second digit is row index.
                new_row.name = str(i + 1) + "r" + str(j + 1)
                new_row.size = 0
                new_row.up = new_row
                new_row.down = new_row
                new_row.left = last_row
                last_row.right = new_row
                last_row = new_row

                #Column column generation
                new_column = Header()
                #First digit is a number that is possible to insert into the column and the second digit is column index.
                new_column.name = str(i + 1) + "c" + str(j + 1)
                new_column.size = 0
                new_column.up = new_column
                new_column.down = new_column
                last_column.right = new_column
                new_column.left = last_column
                last_column = new_column

                #Block column generation
                new_block = Header()
                #First digit is a number that is possible to insert into the block and the second digit is block index (top-leftmost block is 1, bottom-rightmost is 9).
                new_block.name = str(i + 1) + "b" + str(j + 1)
                new_block.size = 0
                new_block.up = new_block
                new_block.down = new_block
                last_block.right = new_block
                new_block.left = last_block
                last_block = new_block

        first_square = first_square.right
        first_row = first_row.right
        first_column = first_column.right
        first_block = first_block.right

        self.__header.right = first_square
        first_square.left = self.__header
        last_square.right = first_row
        first_row.left = last_square
        last_row.right = first_column
        first_column.left = last_row
        last_column.right = first_block
        first_block.left = last_column
        last_block.right = self.__header
        self.__header.left = last_block

        row_iterator = first_row
        column_iterator = first_column
        square_iterator = first_square
        previous_column_iterator = column_iterator #Used when a single row is filled so we could return to columnn 1 but on the next row.
        block_iterator = first_block
        #Used when a signle row (note that every row intersects 3 blocks) is filled a we need to get to a next row intersecting those same 3 blocks.
        previous_block_iterator = block_iterator

        #For each square
        for i in range(81):
            #For each number in one square
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

                #After 3 columns have passed, block number changes
                if ((j + 1) % 3 == 0):
                    block_iterator = block_iterator.right
            #If 3 rows are filled, then move to next 3 blocks belonging to another 3 rows
            if ((i + 1) % 3 == 0):
                    previous_block_iterator = block_iterator
            else: #otherwise return to the first block belonging to current 3 rows
                block_iterator = previous_block_iterator        
            
            #If all 9 rows are filled, move to the 1st column of next number and move to the square on coordinates (1,1)
            if ((i + 1) % 9 == 0):
                previous_column_iterator = column_iterator
                square_iterator = first_square
            else: #otherwise return to the 1st column of the same number
                column_iterator = previous_column_iterator

            row_iterator = row_iterator.right

        #Iterates over the sudoku and deletes the links corresponding with given clues from the user
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
                        #On all but square headers there is information about what number the selected row in constraint grid represents.
                        if (cell_iterator.left.column.name[0:1] == str(number)):
                            self.__found_solutions[self.__solution_count] = cell_iterator
                            self.__solution_count += 1
                            row_iterator = cell_iterator.right
                            while(row_iterator != cell_iterator):
                                self.__cover(row_iterator.column)
                                row_iterator = row_iterator.right
                        cell_iterator = cell_iterator.down

    #Covers (deletes) a column from constraint grid and deletes links to cells in the same row in other columns.
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

    #Reverses the "__cover" function. Uncovering takes place in opposite order (covering from up-down left-right, uncovering down-up right-left)
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

    #Generates solved sudoku from cells that were stored during "__solve" function.
    def __generate_answer(self):
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
                #The value belonging to particular cell is to be found in any row, column or block header
                solution[int(coordinate_cell.column.name[0:1]) - 1][int(coordinate_cell.column.name[1:2]) - 1] = coordinate_cell.right.column.name[0:1]
        self.__solution = solution

    #Finds a header with the smallest size - used for heuristic, which chooses the column with the smallest number for possible solutions.
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

    #Finds a solution that would satisfy all the constraints. If there is no such solution, the property __solution is None. If there is one, the property contains the solution.
    #If there are multiple solution, __answer_count is greater than 1 and there is one of the multiple solutions in __solution.
    def __search(self, k):
        if (self.__answer_count > 1): #We do not need to search for all the solutions
            return
        if (self.__header.right == self.__header):
            self.__generate_answer()
            self.__answer_count += 1
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

    #Constructs the constraint grid and solves it. If there is a solution, then the solution is returned. Otherwise, None is returned.
    def Solve(self, sudoku_matrix = None):
        if (sudoku_matrix == None and self.__original_sudoku != None):
            self.__search(self.__solution_count)
        elif (sudoku_matrix == None and self.__original_sudoku == None):
            return None
        else:
            self.__construct_links(sudoku_matrix)
            self.__search(self.__solution_count)

        return self.__solution

    def get_solution_count(self):
        return self.__answer_count
    
    #Tries to find a constraint with only 1 possible solution. Then an appropriate message is returned.
    def get_hint(self, sudoku_grid):
        self.__construct_links(sudoku_grid)
        column_iterator = self.__header.right
        while(column_iterator.size != 1 and column_iterator != self.__header):
            column_iterator = column_iterator.right
        if (column_iterator == self.__header):
            return "V momentálnom stave nie je možné dať žiadnu nápovedu"
        if (column_iterator.name[1] == "r"):
            return "Na súradnice " + column_iterator.name[2] + " " + column_iterator.down.right.column.name[2] + " je možné dať iba " + column_iterator.name[0]
        elif (column_iterator.name[1] == "c"):
            return "Na súradnice " + column_iterator.down.left.column.name[2] + " " + column_iterator.name[2] + " je možné dať iba " + column_iterator.name[0]
        elif (column_iterator.name[1] == "b"):
            return "Na súradnice " + column_iterator.down.right.column.name[0] + " " + column_iterator.down.right.column.name[1] + " je možné dať iba " + column_iterator.name[0]
        else:
            return "Na súradnice " + column_iterator.name[0] + " " + column_iterator.name[1] + " je možné dať iba " + column_iterator.down.right.column.name[0]