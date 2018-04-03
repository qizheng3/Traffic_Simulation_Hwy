class Cell:
    def __init__(self, gridSize, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
        self.gridSize = gridSize
    
    def resetCell(self, gridSize, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
        self.gridSize = gridSize
