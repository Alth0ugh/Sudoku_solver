class DancingLinks():
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
            found_solutions[k] = row_iterator
            column_iterator = row_iterator.right
            while(column_iterator != row_iterator):
                self.__cover(column_iterator.column)
                column_iterator = column_iterator.right
            self.__search(k+1)
            column_iterator = found_solutions[k].left
            column = found_solutions[k].column
            while (column_iterator != found_solutions[k]):
                self.__uncover(column_iterator.column)
                column_iterator = column_iterator.left
            row_iterator = row_iterator.down
        self.__uncover(column)

    def Solve():
        pass


