import vehicle
import cell
import multilane
import ui
import threading
import settings
import utility


def run(GUI):
    iteration = 100
    vMaxes = [80, 80, 80, 80, 70, 50, 50]
    
    hwy = multilane.MultiLane(settings.UI_BASEMAP, vMaxes)
    for i in range(iteration):
        hwy.exit_at_end()
        hwy.enter_at_start(0.6, 0.4)
        hwy.check_change_left()
        hwy.check_change_right()
        hwy.update_speed()
        hwy.update_position()
        newmap = hwy.get_data()
        x = []
        y = []
        for lanex in newmap:
            for c in lanex.cells:
                if c.veh is not None:
                    x.append(c.x)
                    y.append(c.y)

        # send data to UI
        GUI.display(x, y)

def test_run():
    iteration = 20
    vMaxes = [80, 80, 80, 80, 70, 50, 50]
    
    hwy = multilane.MultiLane (settings.UI_BASEMAP, vMaxes)
    for i in range (iteration):
        hwy.exit_at_end ()
        hwy.enter_at_start (0.4, 0.3)
        hwy.check_change_left ()
        hwy.check_change_right ()
        hwy.update_speed ()
        hwy.update_position ()
        newmap = hwy.get_data ()
        res = []
        for lanex in newmap:
            for c in lanex.cells:
                if c.veh is not None:
                    res.append((c.x, c.y))
            
        print
        print
        print "Run #" + str (i + 1)
        print res
        print
        print

        # send data to UI
        # GUI.display (newmap)
        

def main():
    settings.init()
    # GUI = ui.UI()
    # workerThread = threading.Thread(target=run(GUI))
    # workerThread.setDaemon(True)
    # workerThread.start()
    # GUI.mainloop()
    test_run()

if __name__ == '__main__':
    main()
