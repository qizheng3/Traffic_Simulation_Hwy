import vehicle
import random
import lane
import settings


class MultiLane:
    def __init__(self, basemap, vMaxes):
        # self.exitPt = exitPt
        # self.q = Queue.Queue()
        density = 0.15
        movement = {}
        self.cell_size = settings.CELL_SIZE
        self.lanes = [lane.Lane(basemap[i], vMaxes[0], density) for i in range(5)]
        self.entrances = [lane.Lane(basemap[5+i], vMaxes[1], density) for i in range(2)]
        self.exits = [lane.Lane(basemap[-1]), vMaxes[2], density]

    def check_change_left(self, movement):
        for i in range(1, len(self.lanes)):
            for j in range(len(ln.cells)):
                car = self.lanes[i].cells[j].veh
                if car is None:
                    continue
                # check lane conditions for left-switch
                if car.speed <= 0.7 * car.vMax:
                    leftLaneIsEmpty = True
                    # if there is no vehicle between 100 ft behind and 50 ft ahead
                    k1 = int (100 / self.cell_size)
                    k2 = int (50 / self.cell_size)
                    for k in range (-k1, k2 + 1):
                        # if there is no vehicle between 100 ft behind and 50 ft ahead
                        if k == 0:
                            continue
                        if self.lanes[i - 1].cells[j + k] is not None:
                            leftLaneIsEmpty = False
                            break
                    if leftLaneIsEmpty and random.random () < self.lanes[i].prob_left:
                        if movement[i-1][j] is None:
                            movement[i-1][j] = (i, )
                        lane.removeCar (j)
                        self.lanes[i - 1].addCar (car, j)

    def check_change_right(self):
        for i in range (self.nLane - 1):
            lane = self.lanes[i]
            for j in range (len (lane.cells)):
                if lane.cells[j] is not None:
                    car = lane.cells[j]
                else:
                    continue
                # if this car is allowed to switch the lane
                if car.speed <= 0.7 * car.vMax:
                    rightLaneIsEmpty = True
                    for k in range (-20, 20):
                        if j + k >= 0 and j + k < len (self.lanes[i + 1].cells) and self.lanes[i + 1].cells[
                            j + k] is not None:
                            # if there is no vehicle between 100m behind and ahead
                            rightLaneIsEmpty = False
                            break
                    if rightLaneIsEmpty and random.random () < self.probRight:
                        lane.removeCar (j)
                        self.lanes[i + 1].addCar (car, j)

    # Every second, update vehicles speed of all lanes
    # if speed is lower than the previous vehicle and lower than max speed, then speed up;
    # if speed is higher than the previous vehicle and their distance < 200 meters, then speed = preSpeed;
    def updateSpeed(self):
        for lane in self.lanes:
            prePos = lane.size - 1;
            while (lane.cells[prePos] == None and prePos >= 0):
                prePos = prePos - 1;  # find the vehicle which is closest to the exit of this lane
            firstCar = lane.cells[prePos];
            if firstCar != None:
                firstCar.speed = min (firstCar.speed + 5, firstCar.vMax,
                                      lane.vMax);  # speed up the first car if possible
            start = prePos - 1;
            for i in range (start, -1, -1):
                if lane.cells[i] != None:
                    preCar = lane.cells[prePos];
                    currCar = lane.cells[i];
                    if currCar.speed <= preCar.speed - 1:
                        currCar.speed = min (currCar.vMax, lane.vMax, preCar.speed);
                    elif currCar.speed > preCar.speed and abs (i - prePos) <= 40:
                        currCar.speed = preCar.speed;
                    prePos = i;

    
    def updatePosition(self):
        for lane in self.lanes:
            for i in range (lane.size - 1, -1, -1):
                if lane.cells[i] != None:
                    car = lane.cells[i];
                    speed = car.speed;
                    newPos = i + int (speed / 10);  # calculate which cell this vehicle will move to
                    if newPos >= lane.size:
                        # deal with the situation if this car exits
                        pass
                    elif lane.cells[newPos] == None:
                        lane.cells[newPos] = car;
                    lane.cells[i] = None;

    
    def checkExit(self, prob):
        rlane = self.lanes[self.nLane-1];
        k = int(self.exitPt * len(rlane.cells))
        elane = self.lanes[-1]
        flag = self.allowDirectExit(elane)  # check whether the entrance point of the new hwy is blocked
        # if any car reaches the exit point, check for exit probability
        if rlane.cells[k] is not None and random.random() < prob:
            car = rlane.cells[k]
            if flag and self.q.empty():
                car.speed = min(car.speed * 0.9, elane.vMax)    # new hwy is not blocked
            else:
                car.speed = min(car.speed * 0.1, elane.vMax)    # new hwy is blocked
            self.q.put(car)
            rlane.removeCar(k)
        if not self.q.empty() and flag:
            elane.addCar(self.q.get(), 0)

        
    def allowDirectExit(self, lane):
        for i in range (4):
            if lane.cells[i] is not None:
                return False
        return True

    
    def enterAtStart(self, prob):
        for lane in self.lanes:
            for i in range (3):
                if lane.cells[i] == None:
                    if random.random () < prob:
                        lane.addCar (vehicle.Vehicle (), i)
                        break
  
    
    def exitAtEnd(self):
        for lane in self.lanes:
            for i in range(len(lane.cells) - 6, len(lane.cells)):
                if lane.cells[i] is not None:
                    lane.removeCar(i)

    
    def entranceEvent(self, probExit, probEnter):
        lastLane = self.lanes[-1]
        for i in range (1000, 1000, len (lastLane.cells)):
            j = -1
            while j > -20:
                if lastLane.cells[i + j] is None:
                    j -= 1
                else:
                    rand = random.random()
                    if rand < probExit:
                        lastLane.removeCar(i + j)
                    break
            rand = random.random()
            if rand < probEnter:
                lastLane.addCar (vehicle.Vehicle (), i)
 
    
    def printSpeed(self):
        for lane in self.lanes:
            for i in range (lane.size):
                if lane.cells[i] == None:
                    print "*",
                else:
                    print lane.cells[i].speed,
            print;
