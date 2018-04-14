import vehicle
import random
import lane
import Queue
import settings

# Assume traffic jam at position index=250, on lane 2
class MultiLane:
    def __init__(self, num_L, vMax):
        self.lanes = [];
        self.probRight = 0.9;  # the probability to turn the right lane
        self.probLeft = 0.9;  # the probability to turn the left lane
        self.num_L = num_L
        self.q = Queue.Queue()
        self.cell_size = settings.CELL_SIZE
        self.vMax = vMax
        L = settings.L
        densities = [0.09, 0.08, 0.07, 0.07, 0.07]
        for i in range(num_L):
            self.lanes.append(lane.Lane(L, vMax, densities[i], i))
     
    def update_speed(self):
        for lane in self.lanes:
            lane.update_speed(5, 130, 60, 3)
                
 
    def update_position(self):
        for lane in self.lanes:
            lane.update_position()
                    
 
    def change_left(self):
        L = settings.L
        for i in range (1, self.num_L):
            lane = self.lanes[i]
            for j in range (len (lane.cells)):
                if lane.cells[j] is not None:
                    car = lane.cells[j]
                else:
                    continue
                # switch lanes allowed
                if car.speed <= 0.8 * car.vMax:
                    leftLaneIsEmpty = True
                    for k in range (-int(100/self.cell_size), int(50/self.cell_size)):
                        if j + k < 0 or j + k > L-1:
                            continue
                        # if there is no vehicle between 100ft behind and 50 ft ahead
                        if self.lanes[i - 1].cells[j + k] is not None:
                            leftLaneIsEmpty = False
                            break
                    if leftLaneIsEmpty and random.random() < self.probLeft:
                        lane.RemoveCar(j)
                        car.speed += 2
                        self.lanes[i - 1].addCar(car, j)

    
    def change_right(self):
        L = settings.L
        for i in range (self.num_L - 1):
            lane = self.lanes[i]
            for j in range (len (lane.cells)):
                if lane.cells[j] != None:
                    car = lane.cells[j]
                else:
                    continue
                # if this car is allowed to switch the lane
                if car.speed <= 0.8 * car.vMax:
                    rightLaneIsEmpty = True
                    for k in range (-int(100/self.cell_size), int(50/self.cell_size)):
                        if j + k < 0 or j + k > L - 1:
                            continue
                        if self.lanes[i + 1].cells[j + k] is not None:
                            # if there is no vehicle between 100m behind and ahead
                            rightLaneIsEmpty = False
                            break
                    if rightLaneIsEmpty and random.random() < self.probRight:
                        lane.RemoveCar(j)
                        car.speed += 2
                        self.lanes[i + 1].addCar(car, j)

  
    def enter_at_start(self, iter = iter):
        if iter < 30:
            prob = 0.7
        elif iter < 80:
            prob = 0.4
        elif iter < 200:
            prob = 0.3
        else:
            prob = 0.25
        for i, lane in enumerate(self.lanes):
            for j in range (2):
                if lane.cells[j] == None:
                    if random.random () < prob:
                        lane.addCar(vehicle.Vehicle(base=0, id=i), j*3)
  
    
    def exit_at_end(self):
        for lane in self.lanes:
            for i in range(len(lane.cells) - 8, len(lane.cells)):
                if lane.cells[i] is not None:
                    lane.RemoveCar(i)


    def update_states(self, iter=0, blocked=-1):
        self.exit_at_end ()
        self.enter_at_start (iter=iter)
        # set change-to-right first when the iteration num is even
        # otherwise set priority to change left, altering between
        # 2 cases to eliminate bias
        if (iter % 2 == 0):
            self.change_right ()
            self.change_left ()
        else:
            self.change_left ()
            self.change_right ()
        self.update_speed ()
        self.update_position ()
        
    def printSpeed(self):
        for lane in self.lanes:
            for i in range (lane.size):
                if lane.cells[i] == None:
                    print "*",
                else:
                    print lane.cells[i].speed,
            print;
