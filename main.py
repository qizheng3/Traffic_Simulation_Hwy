import vehicle
import lane
import ui
import threading
import settings
import multilane


def run(GUI):
    iteration = 1000

    hwy = multilane.MultiLane(5, 8, 0.6)
    basemap = settings.UI_BASEMAP

    for i in range (iteration):
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


def main():
    settings.init()
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