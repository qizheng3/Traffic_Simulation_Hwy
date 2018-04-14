import vehicle
import lane
import settings
import multilane
import utility
import highway


settings.init()
iteration = 100
hwy = highway.HighWay ()
basemap = settings.UI_BASEMAP


for i in range (iteration):
    hwy.update_states ()
    # x = [[] for _ in range (len (res))]
    # y = [[] for _ in range (len (res))]

res = hwy.multiway.lanes

print res

# print len(res)
# print "-----------------------------"
# for lane in res:
#     print(len(lane.cells))

# print
# print "-----------------------------"
# print len(basemap)
# for b in basemap:
#     print(len(b))