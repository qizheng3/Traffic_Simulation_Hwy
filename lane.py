import vehicle
import random
import cell
import settings

# one single lane
class Lane:
    def __init__(self, coords, vMax, density=0.1, prob_left=0, prob_right=0):
        # density = total number of vehicles / total number of cells
        self.density = density  # initialize the vehicle density of one highway
        self.vMax = vMax  # max speed for all vehicles in this lane
        self.size = len(coords)	# initialize the number of cells of one highway (unit length: 10 meters) #### updated: 5m
        self.cells = [cell.Cell(xi, yi) for (xi, yi) in coords]# initialize the cell array
        self.prob_left = prob_left
        self.prob_right = prob_right
        
        # initialize some vehicles in the lane
        for i in range(int(self.density * self.size)):
            position = 0;
            while True:
                position = random.randint(0, self.size - 1);
                if self.cells[position].veh is None:
                    break;
            self.cells[position].veh = vehicle.Vehicle();
        
        self.vNum = int(self.density * self.size);  # number of vehicles in this lane
        self.hasAccident = False;  # one lane has no car accidents at the beginning
    
    # add a new vehicle into a given position of one lane
    def addCar(self, car, position):
        if self.cells[position].veh is None:
            self.cells[position].veh = car;
            self.vNum = self.vNum + 1;
            return True;
        else:
            return False;
    
    def removeCar(self, position):
        if (self.cells[position].veh is not None):
            car = self.cells[position].veh;
            self.vNum = self.vNum - 1;
            self.cells[position].veh = None;
            return car;
    
    # get some system status of this lane (e.g., density, occurence of accidents)
    def getPara(self):
        self.density = self.vNum / self.size;
        return self.density, self.hasAccident;
