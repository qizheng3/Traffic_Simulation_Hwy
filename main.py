
import threading
import highway
import multilane
import settings
import ui
import time
import random

def run(GUI):
    iteration = 200
    traffic = 50
    acc_start = 30
    hwy = highway.Highway ()
    basemap = settings.UI_BASEMAP
    for it in range (iteration):
        
        hwy.update_states(itern=it)
        
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
    random.seed(time.time ())
    print settings.UI_BASEMAP[1][250]
    GUI = ui.UI()
    workerThread = threading.Thread(target=run, args=(GUI,))
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