import random
import time
random.seed(time.time())


class Vehicle:
    def __init__(self, base=0, id=-1):
        self.vMax = random.randint(8-base, 10-base)
        self.speed = random.randint(3-int(base/3), 10-base);
        self.id = id
        # initialize the speed of one vehicle
        
    def changeSpeed(self, v):
        self.speed = v
