import random

class Vehicle:
    def __init__(self):
        # there are three types of vehicles. Their max speed is 25m/s, 30m/s, 35m/s, respectively
        # the probability of this three types is: 0.2, 0.5, 0.3
        self.vMax = 35;
        rand = random.random();
        if (rand <= 0.2):
            self.vMax = 25;
        elif (rand <= 0.7):
            self.vMax = 30;
        
        self.speed = max(17, random.random() * self.vMax);
        # initialize the speed of one vehicle, assume the minimal speed is 17m/s (60km/s)
        
        
        self.probChangeWay = 0.3;  # the probability to turn to another highway if it's in the rightmost lane
    
    def changeSpeed(self, v):
        self.speed = v;
