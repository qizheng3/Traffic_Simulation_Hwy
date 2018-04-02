import vehicle
import HighWay
import Lane
import UI
import threading


def main():
    GUI = UI.UI()
    
    def run():
        highwayLength = 3000
        vMax1 = 45
        vMax2 = 25
        nLane = 3

        highways = HighWay.HighWay(highwayLength, nLane, vMax1, vMax2)
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
    
    workerThread = threading.Thread(target=run)
    workerThread.setDaemon(True)
    workerThread.start()
    
    GUI.mainloop()


if __name__ == '__main__':
    main()
