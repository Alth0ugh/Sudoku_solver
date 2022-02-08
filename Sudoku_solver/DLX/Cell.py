#Class representing a single cell in constraint grid.
class Cell(object):
    def __init__(self):
        #Up, down, left, right contain reference to cell's respective neighbouting cells/headers.
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        #Contains reference to the column the cell belongs to. If the cell is in the first row from the top, it referes to the same object as 'up' property.
        self.column = None


