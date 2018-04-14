import multilane


class HighWay:
    def __init__(self, highwayLength, nLane, vMax1, vMax2):
        self.multiway = multilane.MultiLane (5, 8, 0.6)
        

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
