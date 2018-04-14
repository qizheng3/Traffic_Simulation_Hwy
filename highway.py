import multilane
import merge
import exit
import random
import settings

class HighWay:
    def __init__(self):
        self.multiway = multilane.MultiLane (5, 8, 0.6)
        self.mergelane = merge.MergeLane(40, 40)
        self.exitway = exit.ExitLane(40)
        

    def update_states(self):
        self.merge_join()
        self.exit_leave(0.9)
        self.multiway.update_states()
        self.mergelane.update_states()
        self.exitway.update_states()
        

    def merge_join(self):
        joins = settings.JOIN_ID[:2]
        for k in range(2):
            dt = 0
            for i in range (1, 4):
                car = self.mergelane.lanes[k].cells[-i]
                if car != None:
                    pos = i
                    break
            if car != None:
                for pt in range(joins[k], joins[k]+80):
                    if all(c == None for c in self.multiway.lanes[k].cells[pt-8: pt+5]):
                        self.mergelane.lanes[k].cells[-pos] = None
                        if random.random()<0.5:
                            car.speed = 5
                        else:
                            car.speed = 6
                        self.multiway.lanes[4].cells[pt] = car
                        break
    
    def exit_leave(self, prob):
        join = settings.JOIN_ID[2]
        for i in range(5):
            car = self.multiway.lanes[4].cells[i+join]
            if car != None:
                if random.random()<prob and self.exitway.lanes.cells[0] == None:
                    randx = random.random ()
                    if randx < 0.1:
                        car.speed = 3
                    elif randx < 0.8:
                        car.speed = 4
                    else:
                        car.speed = 5
                    self.exitway.lanes.cells[0] = car
                    self.multiway.lanes[4].cells[i + join] = None
                break
                