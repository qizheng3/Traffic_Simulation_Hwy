import random

class Vehicle:
    def __init__(self, id=-1):
        self.vMax = random.randint(8, 10)
        self.speed = random.randint(3, 10);
        self.id = id
        # initialize the speed of one vehicle
        
    def changeSpeed(self, v):
        self.speed = v;
