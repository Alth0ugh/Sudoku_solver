from DLX.Cell import *

#Class containing information about a header in a constraint grid.
class Header(Cell):
    def __init__(self):
        self.name = None
        #Number of cells in a column represented by the header.
        self.size = None