from DLX.Cell import *
from DLX.Header import *

class DancingLinks():
    def __init__(self):
        self.__found_solutions = []
        self.__header = Header()

    def __construct_links(self, sudoku_matrix):
        header_iterator = self.__header
        header_iterator.name = "master"
        first_row = None
        first_column = None
        first_block = None
        
        for i in range(9):
            for j in range(9):
                new_column = Header()
                new_column.name = str(i + 1) + "r" + str(j + 1)
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
        previous_column_iterator = column_iterator
        block_iterator = first_block
        previous_block_iterator = block_iterator
        #i = 0
        #j = 0
        #while (i < 81):
        #    new_row_cell = Cell()
        #    new_column_cell = Cell()
        #    new_block_cell = Cell()

        #    new_row_cell.right = new_column_cell
        #    new_row_cell.left = new_block_cell
            
        #    new_column_cell.left = new_row_cell
        #    new_column_cell.right = new_block_cell

        #    new_block_cell.right = new_row_cell
        #    new_block_cell.left = new_column_cell

        #    #Insert row cell
        #    new_row_cell.down = row_iterator.down
        #    row_iterator.down.up = new_row_cell
        #    row_iterator.down = new_row_cell

        #    new_row_cell.up = row_iterator
        #    new_row_cell.column = row_iterator

        #    #Insert column cell
        #    new_column_cell.down = column_iterator.down
        #    column_iterator.down.up  = new_column_cell
        #    column_iterator.down = new_column_cell

        #    new_column_cell.up = column_iterator
        #    new_column_cell.column = column_iterator

        #    #Insert block cell
        #    new_block_cell.down = block_iterator
        #    block_iterator.down.up = new_block_cell
        #    block_iterator.down = new_block_cell

        #    new_block_cell.up = block_iterator
        #    new_block_cell.column = block_iterator

        #    column_iterator = column_iterator.right
            
        #    if ((j + 1) % 81 == 0):
        #        previous_column_iterator = column_iterator
        #    elif ((j + 1) % 9 == 0):
        #        column_iterator = previous_column_iterator

        #    if ((j + 1) % 27 == 0):
        #        block_iterator = block_iterator.right
        #        previous_block_iterator = block_iterator
        #    elif ((j + 1) % 9 == 0):
        #        block_iterator = previous_block_iterator
        #    elif ((j + 1) % 3 == 0):
        #        block_iterator = block_iterator.right

        #    row_iterator = row_iterator.right
        #    i += 1
        #    j += 1

        for i in range(81):
            for j in range(9):
                new_row_cell = Cell()
                new_column_cell = Cell()
                new_block_cell = Cell()

                new_row_cell.right = new_column_cell
                new_row_cell.left = new_block_cell
                
                new_column_cell.left = new_row_cell
                new_column_cell.right = new_block_cell

                new_block_cell.right = new_row_cell
                new_block_cell.left = new_column_cell

                #Insert row cell
                new_row_cell.down = row_iterator.down
                row_iterator.down.up = new_row_cell
                row_iterator.down = new_row_cell

                new_row_cell.up = row_iterator
                new_row_cell.column = row_iterator

                #Insert column cell
                new_column_cell.down = column_iterator.down
                column_iterator.down.up  = new_column_cell
                column_iterator.down = new_column_cell

                new_column_cell.up = column_iterator
                new_column_cell.column = column_iterator

                #Insert block cell
                new_block_cell.down = block_iterator
                block_iterator.down.up = new_block_cell
                block_iterator.down = new_block_cell

                new_block_cell.up = block_iterator
                new_block_cell.column = block_iterator

                column_iterator = column_iterator.right

                if ((j + 1) % 3 == 0):
                    block_iterator = block_iterator.right
            
            if ((i + 1) % 3 == 0):
                    previous_block_iterator = block_iterator
            else:
                block_iterator = previous_block_iterator        
                    
            if ((i + 1) % 9 == 0):
                previous_column_iterator = column_iterator
            else:
                column_iterator = previous_column_iterator

            row_iterator = row_iterator.right

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
                down_element = column_iterator

                left_column = column_iterator.column.left
                right_column = column_iterator.column.right

                column_iterator = column_iterator.left
            row_iterator = row_iterator.up

    def __search(self, k = 0):
        if (header.right == header):
            print_answer()
            return
        column = header.right
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

    def Solve(self):
        #self.__search()
        #return self.__found_solutions
        self.__construct_links(None)