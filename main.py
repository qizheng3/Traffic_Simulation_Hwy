
import threading
import highway
import multilane
import settings
import ui
import time
import random

def run(GUI):
    iteration = 5000
    acc_start = 500
    acc_stop = 2000
    hwy = highway.Highway ()
    basemap = settings.UI_BASEMAP
    accident = "ON"                 # toggle between ON and OFF
    traffic_light = "OFF"            # toggle between ON and OFF
    traff_intv = 100
    traff_dura = 90
    light = ["Yello", "Green", "Red"]
    ind = 1
    for itr in range (iteration):

        if accident == "ON":
            # Interface for calling traffic accidents: hwy.update_states(itr, flag)
            # flag = 1: traffic accident; flag = 0: no accident
            if itr < acc_start or itr > acc_stop:
                hwy.update_states(itr, 1)
            else:
                hwy.update_states(itr, 0)
        
        if traffic_light == "ON":
            if itr % (traff_intv + traff_dura) == 0:
                hwy.mergelane.e_prob1 = 0
            elif itr % (traff_intv + traff_dura) == traff_intv:
                hwy.mergelane.e_prob1 = 0.7
            if itr == iteration - 1:
                hwy.mergelane.e_prob1 = 0.5
            hwy.update_states (itr, 0)
        
        if accident == "OFF" and traffic_light == "OFF":
            hwy.update_states (itr, 0)
        
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
    # print settings.UI_BASEMAP[1][250]
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