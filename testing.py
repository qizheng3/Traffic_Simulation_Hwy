import vehicle
import lane
import settings
import multilane
import utility

iteration = 3
settings.init()
hwy = multilane.MultiLane (5, 8, 0.6)
basemap = settings.UI_BASEMAP

for i in range (iteration):
    hwy.exit_at_end ()
    hwy.enter_at_start (0.4)
    # hwy.change_left ()
    # hwy.change_right ()
    hwy.update_speed ()
    hwy.update_position ()


x = [[]] * 5
y = [[]] * 5
for i, lanex in enumerate (hwy.lanes):
    for j, c in enumerate (lanex.cells):
        if c != None:
            id = c.id
            # if id != i:
            #     print '(', id, ',', i, ')',
            xi, yi = basemap[i][j]
            x[i].append (xi)
            y[i].append (yi)
    print len(x[i]), len(y[i])
    l = len(hwy.lanes[i].cells)
    print l - hwy.lanes[i].cells.count(None)

