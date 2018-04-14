
import threading

import highway
import multilane
import settings
import ui


def run(GUI):
    iteration = 1000

    hwy = multilane.MultiLane(5, 8, 0.6)
    basemap = settings.UI_BASEMAP

    for iter in range (iteration):
        hwy.exit_at_end ()
        hwy.enter_at_start (0.4)
        hwy.change_left ()
        hwy.change_right ()
        hwy.update_speed ()
        hwy.update_position ()
        x = [[] for _ in range(5)]
        y = [[] for _ in range(5)]
        for i, lanex in enumerate(hwy.lanes):
            for j, c in enumerate(lanex.cells):
                if c != None:
                    id = c.id
                    xi, yi = basemap[i][j]
                    x[id].append (xi)
                    y[id].append (yi)

        # send data to UI
        GUI.sendMessage (x, y)


def test_run(GUI):
    iteration = 1000
    hwy = highway.HighWay ()
    basemap = settings.UI_BASEMAP
    for iter in range (iteration):
        hwy.update_states ()
        res1 = hwy.multiway.lanes
        res2 = hwy.mergelane.lanes
        res3 = hwy.exitway.lanes
        x = [[] for _ in range (8)]
        y = [[] for _ in range (8)]
        for i, lanex in enumerate (res1):
            for j, c in enumerate (lanex.cells):
                if c != None:
                    id = c.id
                    xi, yi = basemap[i][j]
                    x[id].append (xi)
                    y[id].append (yi)
                    
        for i, lanex in enumerate (res2):
            for j, c in enumerate (lanex.cells):
                if c != None:
                    id = c.id
                    xi, yi = basemap[i+5][j]
                    x[id].append (xi)
                    y[id].append (yi)
                    
        for j, c in enumerate(res3.cells):
            if c != None:
                id = c.id
                xi, yi = basemap[7][j]
                x[id].append (xi)
                y[id].append (yi)
                
        # send data to UI
        GUI.sendMessage (x, y)

# 8 -- 518, 518, 518, 518, 518, 136, 163, 111

def main():
    settings.init()
    GUI = ui.UI()
    workerThread = threading.Thread(target=test_run, args=(GUI,))
    workerThread.setDaemon(True)
    workerThread.start()
    # run(GUI)
    painterThread = threading.Thread(target=GUI.processMessage)
    painterThread.setDaemon(True)
    painterThread.start()
    # GUI.processMessage()

    GUI.mainloop()
    # test_run()

if __name__ == '__main__':
    main()


# hwy = MultiLane.MultiLane(5, 8, 0.6)
#
# print len(hwy.lanes)