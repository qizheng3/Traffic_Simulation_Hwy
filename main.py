import vehicle
import highway
import lane
import ui
import threading
from config import *

def run(GUI):
    highwayLength = 3000
    vMax1 = 45
    vMax2 = 35
    nLane = 3
    
    highways = highway.Highway(highwayLength, nLane, vMax1, vMax2)
    iteration = 1000
    
    for i in range(iteration):
        # highway.printSpeed();
        # highway.updateSpeed()
        # highway.updatePosition()
        # highway.checkChangeLaneLeft()
        # highway.checkChangeLaneRight()
        # highway.enterAtStart(0.1)
        # highway.exitAtEnd()
        # highway.entranceEvent(0.3, 0.4)
        
        highways.updateStates()
        
        # send data to UI
        GUI.display(highways)

def main():
    # GUI = ui.UI()
    #
    # workerThread = threading.Thread(target=run(GUI))
    # workerThread.setDaemon(True)
    # workerThread.start()
    #
    # GUI.mainloop()




if __name__ == '__main__':
    main()
