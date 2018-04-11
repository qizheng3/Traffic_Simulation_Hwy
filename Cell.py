class Cell:
    def __init__(self, x, y, road=None, veh=None):
        self.x = x
        self.y = y
        self.road = road
        self.veh = veh
        self.state = None
    
    def update(self, x=None, y=None, road=None, veh=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if road is not None:
            self.road = road
        if veh is not None:
            self.veh = veh

    def get_param(self):
        return self.road, self.x, self.y, self.veh
