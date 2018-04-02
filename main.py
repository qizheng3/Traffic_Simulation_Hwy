import vehicle
import MultiLane
import Lane
import UI
import threading


def main():
    GUI = UI.UI()
    
    def run():
        highwayLength = 2500
        vMax = 40
        nLane = 3
        exitPt = 0.3
<<<<<<< HEAD
        densityEntrance = 0.1
        probEnter = 0.3
        probExit = 0.4
=======
>>>>>>> 05ef8ec4e791b21a8e0ec36a4e08439ed14116c3
        highway = MultiLane.MultiLane(highwayLength, 2 * nLane, exitPt, vMax)
        
        iteration = 400
        
        for i in range(iteration):
            # highway.printSpeed();
            highway.updateSpeed()
            highway.updatePosition()
            highway.checkChangeLaneLeft()
            highway.checkChangeLaneRight()
<<<<<<< HEAD
            highway.enterAtStart(densityEntrance)
            highway.exitAtEnd()
            highway.entranceEvent(probEnter, probExit)
=======
            highway.enterAtStart(0.1)
            highway.exitAtEnd()
            highway.entranceEvent(0.3, 0.4)
>>>>>>> 05ef8ec4e791b21a8e0ec36a4e08439ed14116c3
            
            # send data to UI
            GUI.display(highway)
    
    workerThread = threading.Thread(target=run)
    workerThread.setDaemon(True)
    workerThread.start()
    
    GUI.mainloop()


if __name__ == '__main__':
    main()
