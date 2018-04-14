import settings
import lane
import random
import vehicle


class ExitLane:
    # 40 ft/s for exit lanes: 4 cells/s
    def __init__(self, vMax):
        ln = settings.L3
        self.lanes = lane.Lane (ln, vMax, 0.1, 7)
        self.cell_size = settings.CELL_SIZE
    
    def update_speed(self):
        self.lanes.update_speed (3, 70, 50, 1, end=True)
    
    def update_position(self):
        for lane in self.lanes:
            lane.update_position (end=True, end_pts=3)
    
    def exit_at_end(self):
       for i in range(len(self.lanes) - 5, len(self.lanes)):
            if lane.cells[i] is not None:
                    lane.RemoveCar(i)
    
    def enter_at_start(self, prob):
        for j in range (2):
            if lane.cells[j] == None:
                if random.random () < prob:
                    lane.addCar(vehicle.Vehicle(7), j)
    
    def update_states(self):
        self.enter_at_start(0.7)
        self.exit_at_end()
        self.update_speed()
        self.update_position()
