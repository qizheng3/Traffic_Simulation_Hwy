from settings import *

class Cell:
    def __init__(self, (xCoord, yCoord)):
        self.id = id
        self.x = xCoord
        self.y = yCoord

    def reset_cell(self, (xCoord, yCoord)):
        self.id = id
        self.x = xCoord
        self.y = yCoord

    def get_param(self):
        return self.id, self.x, self.y
