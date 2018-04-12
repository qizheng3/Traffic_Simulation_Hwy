import vehicle
import random
import lane
import settings
import Queue

class MultiLane:
    def __init__(self, basemap, vMaxes):
        # self.exitPt = exitPt
        # self.q = Queue.Queue()
        density = 0.15
        self.exitprob = 0.8
        self.cell_size = settings.CELL_SIZE
        self.lanes = [lane.Lane(basemap[i], vMaxes[i], density) for i in range(5)]
        self.entrances = [lane.Lane(basemap[5+i], vMaxes[5], density) for i in range(2)]
        self.exit = lane.Lane(basemap[-1], vMaxes[6], density)
        self.movement = [[None for _ in range(len(l.cells))] for l in self.lanes]
        self.ex = Queue.Queue()
        self.en1 = Queue.Queue()
        self.en2 = Queue.Queue()

    # probs: (prob1: main hwy, prob2: sub hwy)
    def enter_at_start(self, prob1, prob2):
        for i, lanex in enumerate(self.lanes):
            for j in range (4, 8):
                if lanex.cells[j].veh is None and random.random () < prob1:
                    lanex.addCar (vehicle.Vehicle(origin=i), j)
        for i in range(2):
            for j in range (2, 5):
                if self.entrances[i].cells[j].veh is None and random.random () < prob2:
                    self.entrances[i].addCar (vehicle.Vehicle(i + 5), j)


    # remove at the end
    def exit_at_end(self):
        for lanex in self.lanes:
            for i in range (-1, -9, -1):
                if lanex.cells[i].veh is not None:
                    lanex.removeCar (i)
        for i in range(-1, -7, -1):
            if self.exit.cells[i].veh is not None:
                self.exit.removeCar(i)
    
    def check_change_left(self):
        print
        for i in range(1, len(self.lanes)):
            lanex = self.lanes[i]
            print len(self.lanes[i].cells)
            for j in range(11, len(lanex.cells)-11):
                car = lanex.cells[j].veh
                if car is None:
                    continue
                # check lane conditions for left switch
                if car.speed <= 0.7 * car.vMax:
                    leftLaneIsEmpty = True
                    # if there is no vehicle between 100 ft behind and 50 ft ahead
                    k1 = int (100 / self.cell_size)
                    k2 = int (50 / self.cell_size)
                    for k in range (-k1, k2 + 1):
                        # if there is no vehicle between 100 ft behind and 50 ft ahead
                        if self.lanes[i - 1].cells[j + k].veh is not None:
                            leftLaneIsEmpty = False
                            break
                    if leftLaneIsEmpty and random.random () < self.lanes[i].prob_left:
                        if self.movement[i - 1][j] is None:
                            self.movement[i - 1][j] = (i, j)
                        elif random.random () < 0.5:
                            self.movement[i-1][j] = (i, j)

                # for j in range (len (self.lanes[4].cells)):
                #     if self.lanes[4].cells[j].veh is None or self.lanes[4].cells[j].veh is not None:
                #         continue
                #     k3 = int (60 / self.cell_size)
                #     k4 = int (40 / self.cell_size)
                #     leftLaneIsEmpty = True
                #     if j >= settings.JOIN_ID[0] and j < settings.JOIN_ID[1] or j > settings.JOIN_ID[2]:
                #         prob = self.lanes[-1].prob_left
                #     else:
                #         prob = 0.7
                #     for k in range (-k3, k4 + 1):
                #         if self.lanes[-1].cells[i + k].veh is not None:
                #             leftLaneIsEmpty = False
                #             break
                #     if leftLaneIsEmpty and random.random () < prob:
                #         self.movement[-2][j] = (-1, j)


    def check_change_right(self):
        for i in range(len(self.lanes)-1):
            for j in range(11, len(self.lanes[i].cells)-11):
                car = self.lanes[i].cells[j].veh
                if car is None:
                    continue
                # check lane conditions for left-switch
                if car.speed <= 0.7 * car.vMax:
                    rightLaneIsEmpty = True
                    # if there is no vehicle in the range [100 ft behind ~ 50 ft ahead]
                    k1 = int (100 / self.cell_size)
                    k2 = int (50 / self.cell_size)
                    for k in range (-k1, k2 + 1):
                        # if there is no vehicle between 100 ft behind and 50 ft ahead
                        if self.lanes[i + 1].cells[j + k].veh is not None:
                            rightLaneIsEmpty = False
                            break
                    if rightLaneIsEmpty and random.random () < self.lanes[i].prob_right:
                        if self.movement[i + 1][j] is None:
                            self.movement[i + 1][j] = (i, j)
                        elif random.random () < 0.5:
                            self.movement[i + 1][j] = (i, j)
            
            # lane3 = self.lanes[3]
            # for j in range(len(lane3.cells)):
            #     if lane3.cells[j].veh is None or self.lanes[-1].cells[j].veh is not None:
            #         continue
            #     k3 = int(60 / self.cell_size)
            #     k4 = int(40 / self.cell_size)
            #     prob = lane3.prob_right
            #     if j > settings.JOIN_ID[1] and j < settings.JOIN_ID[2] + 1:
            #         prob = 0
            #     rightLaneIsEmpty = True
            #     for k in range(-k3, k4+1):
            #         if lane3.cells[j + k].veh is not None:
            #             rightLaneIsEmpty = False
            #             break
            #     if rightLaneIsEmpty and random.random () < prob:
            #             self.movement[-1][j] = (-2, j)


    def update_speed_util(self, lanex, lim, lookahead, vlim, dv):
        curr = 0
        q = Queue.Queue ()
        while curr < lim - 1:
            if lanex.cells[curr].veh is None:
                curr += 1
            else:
                j = curr + 1
                while j < min (curr + lookahead + 1, lim):
                    if lanex.cells[j].veh is not None:
                        break
                    j += 1
                # slow down to avoid collision
                if j < lim and lanex.cells[j].veh is not None:
                    if lanex.cells[j].veh.speed < lanex.cells[curr].veh.speed:
                        v_new = lanex.cells[j].veh.speed
                        v_curr = lanex.cells[curr].veh.speed
                        if j <= curr + int(v_curr/self.cell_size):
                            v_new *= 0.6
                        q.put ((curr, min (v_new, vlim)))
                # speed up if possible (no blocking)
                else:
                    if lanex.cells[curr].veh.speed < 10:
                        lanex.cells[curr].veh.speed = 25 + lanex.cells[curr].veh.speed//2
                    q.put ((curr, min (lanex.cells[curr].veh.speed + dv, vlim)))
                curr = j
    
        while not q.empty ():  # when finish one lane, update it
            pos, spd = q.get ()
            lanex.cells[pos].veh.speed = spd


    # Every frame, first update vehicles speed of all lanes
    # Speed limit: 55mph on i-75/85 near downtown Atlanta (80 ft/sec)
    # refresh frequency: 0.5 sec
    def update_speed(self):
        
        # first update positions (lane switch, no advancing)
        for i in range(len(self.movement)):
            for j in range(len(self.movement[i])):
                if self.movement[i][j] is not None:
                    ri, rj = self.movement[i][j]
                    temp_car = self.lanes[ri].removeCar(rj)
                    self.lanes[i].addCar(temp_car, j)
                    self.movement[i][j] = None
        
        # then update speed, speed of any vehicle is only affected by
        # a vehicle car <= 120ft (lookahead 120ft ~ <= 1.25 sec to arrive) away
        for i in range(len(self.lanes)):
            lim = len(self.lanes[i].cells)
            if i <= 3:
                lookahead = int(120/self.cell_size)
                dv = 10
            else:
                lookahead = int(70/self.cell_size)
                dv = 5
            vlim = self.lanes[i].vMax + 5
            self.update_speed_util(self.lanes[i], lim, lookahead, vlim, dv)
        
        # similarly, update the speed of vehicles on 2 merge hwys
        for i in range(len(self.entrances)):
            lim = len (self.entrances[i].cells)
            lookahead = int (50 / self.cell_size)
            dv = 5
            vlim = self.entrances[i].vMax + 5
            self.update_speed_util (self.entrances[i], lim, lookahead, vlim, dv)

        lim = len (self.exit.cells)
        lookahead = int (50/self.cell_size)
        dv = 5
        vlim = self.exit.vMax + 5
        self.update_speed_util (self.exit, lim, lookahead, vlim, dv)


    def update_position(self):
        dt = 0.5
        # update 2 merge lanes
        for i in range(2):
            merge_pos = settings.JOIN_ID[i]
            for k in range(merge_pos, merge_pos + int(180/self.cell_size) + 1):
                flag = True
                for j in range(-2, 2):
                    if self.lanes[4].cells[k+j].veh is not None:
                        flag = False
                        break
                if flag:
                    break

            if flag and not self.en1.empty ():
                car = self.en1.get ()
                self.lanes[4].addCar (car, k)
                
            lanex = self.entrances[i]
            l1 = len (lanex.cells)
            for i, cellx in enumerate (lanex.cells):
                if cellx.veh is not None:
                    speed = cellx.veh.speed
                    newPos = i + int (speed * dt / self.cell_size)  # calculate which cell this vehicle will move to
                    car = lanex.removeCar (i)
                    # n = self.en1.qsize ()
                    if newPos > l1 - 1:
                        self.en1.put (car)
                    elif lanex.cells[newPos].veh is None:
                        lanex.addCar (car, newPos)
   
        # update the exit lane:
        exit_pos = settings.JOIN_ID[2]
        lanex = self.lanes[4]
        for j in range(1, -3, -1):
            car = lanex.cells[exit_pos + j].veh
            if car is not None:
                if random.random() < self.exitprob:
                    lanex.removeCar(exit_pos + j)
                    self.ex.put(car)
                    break
        
        if not self.ex.empty() and self.exit.cells[0].veh is None:
            car = self.ex.get()
            self.exit.addCar(car, 0)
            
        # update lane 0-4 (5 lanes)
        for lanex in self.lanes:
            l = len (lanex.cells)
            for i, cellx in enumerate (lanex.cells):
                if cellx.veh is not None:
                    speed = cellx.veh.speed
                    newPos = i + int (speed * dt / self.cell_size);  # calculate which cell this vehicle will move to
                    car = lanex.removeCar (i)
                    if newPos > l-2:  # deal with the situation if this car exits
                        pass
                    elif lanex.cells[newPos].veh is None:
                        lanex.addCar (car, newPos)
        

    def get_data(self):
        res = self.lanes
        res.extend(self.entrances)
        res.append(self.exit)
        return res

