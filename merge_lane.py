import settings
import lane

class MergeLane:
    # 40 ft/s for in-merging lanes: 4 cells/s
    def __init__(self, vMax1, vMax2):
        vm = [vMax1, vMax2]
        ln = [settings.L1, settings.L2]
        self.lanes = [lane.Lane(ln[i], vm[i], 0.05, i+5) for i in range(2)]
        self.cell_size = settings.CELL_SIZE
    
    def update_speed(self):
        for lane in self.lanes:
            lane.update_speed(4, 70, 50, 1)

    def update_position(self):
        for lane in self.lanes:
            lane.update_position(end=True, end_pts=3)
    
    
