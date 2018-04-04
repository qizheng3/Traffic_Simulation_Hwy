class Cell:
    def __init__(self, ID， xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
        self.ID = ID
    
    def resetCell(self, ID, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
        self.ID = ID
