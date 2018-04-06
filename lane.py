import vehicle
import random

cell_size = 5

# one single lane
class Lane:
    def __init__(self, base_array, vMax, density):
        # density = total number of vehicles / total number of cells
        self.density = density  # initialize the vehicle density of one highway
        self.vMax = vMax  # max speed for all vehicles in this lane
        self.size = len(base_array)	# initialize the number of cells of one highway (unit length: 10 meters) #### updated: 5m
        self.cells = [None] * self.size  # initialize the cell array
        
        # initialize some vehicles in the lane
        for i in range(int(self.density * self.size)):
            position = 0;
            while True:
                position = random.randint(0, self.size - 1);
                if self.cells[position] == None:
                    break;
            self.cells[position] = vehicle.Vehicle();
        
        self.vNum = int(self.density * self.size);  # number of vehicles in this lane
        self.hasAccident = False;  # one lane has no car accidents at the beginning
    
    # add a new vehicle into a given position of one lane
    def addCar(self, car, position):
        if (self.cells[position] == None):
            self.cells[position] = car;
            self.vNum = self.vNum + 1;
            return True;
        else:
            return False;
    
    def RemoveCar(self, position):
        if (self.cells[position] != None):
            car = self.cells[position];
            self.vNum = self.vNum - 1;
            self.cells[position] = None;
            return car;
    
    # get some system status of this lane (e.g., density, occurence of accidents)
    def getPara(self):
        self.density = self.vNum / self.size;
        return self.density, self.hasAccident;
