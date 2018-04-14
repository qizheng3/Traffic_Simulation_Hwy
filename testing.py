import vehicle
import lane
import settings
import multilane
import utility
import highway


settings.init()
iteration = 1
hwy = highway.HighWay ()
basemap = settings.UI_BASEMAP


iteration = 10
hwy = highway.HighWay ()
basemap = settings.UI_BASEMAP
for iter in range (iteration):
    hwy.update_states ()
    res1 = hwy.multiway.lanes
    res2 = hwy.mergelane.lanes
    res3 = hwy.exitway.lanes

for j, c in enumerate (res3.cells):
    if c != None:
        id = c.id
        print id
        
print len(res3.cells)