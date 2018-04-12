import random

class Vehicle:
    def __init__(self, origin=None):
        # there are three types of vehicles. Their max speed is 80ft/s (55mph), 70ft/s, 60ft/s (41 mph), respectively
        # the probability of this three types is: 0.3, 0.3, 0.4
        self.origin = origin
        v = 60 + random.random() * 25
        self.vMax = v
        self.speed = v

