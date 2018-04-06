from config import *

class Cell:
    def __init__(self, id, (xCoord, yCoord)):
        self.id = id
        self.x = xCoord
        self.y = yCoord

    def reset_cell(self, id, xCoord, yCoord):
        self.id = id
        self.x = xCoord
        self.y = yCoord

    def get_param(self):
        return self.id, self.x, self.y
