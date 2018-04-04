import multilane


class Highway:
    def __init__(self, highwayLength, nLane, vMax1, vMax2):
        self.RL = multilane.MultiLane(highwayLength, 1530, nLane, vMax1, vMax2, 0.6);
        self.LL = multilane.MultiLane(highwayLength, 2500, nLane, vMax1, vMax2, 0.3);
    
    def updateStates(self):
        for hwy in (self.LL, self.RL):
            hwy.updateSpeed()
            hwy.updatePosition()
            hwy.checkChangeLaneLeft()
            hwy.checkChangeLaneRight()
            hwy.checkExit(0.1)
            hwy.enterAtStart(0.2)
            hwy.exitAtEnd()
            # hwy.entranceEvent(0.3, 0.4)
