import numpy as np
import matplotlib.pyplot as plt
import math

global CELL_SIZE
global JOIN_ID
global HWY75
global SUB_RD
global TRAFFIC
global MAPS


scale = 5.8
origin = (610, 861)
join_pos = [1, 0.33, 0]
traffic_lane = [985, 910]


CELL_SIZE = 20
HWY75 = [(1132, 917), (1065, 695), (722, 339), (539, 219)]
SUB_RD = [(1170, 918), (1225, 690), (617, 160)]


HWY75 = [(x - origin[0], -y + origin[1]) for (x, y) in HWY75]
SUB_RD = [(x - origin[0], -y + origin[1]) for (x, y) in SUB_RD]

HWY75 = [(x * scale, y * scale) for (x, y) in HWY75]
SUB_RD = [(x * scale, y * scale) for (x, y) in SUB_RD]
# print HWY75
# Now HWY75 = [(3027.6, 324.8), (2639.0, -962.8), (649.6, -3027.6), (-411.8, -3723.6)]

Lh = [(HWY75[i+1][0] - HWY75[i][0])**2 + (HWY75[i+1][1] - HWY75[i][1])**2 for i in range(len(HWY75)-1)]
Lh = [math.sqrt(lx) for lx in Lh]
# print Lh

num_cells = [int(l/CELL_SIZE + 0.5) for l in Lh]
# print num_cells

JOIN_ID = [num_cells[0], num_cells[0] + int(num_cells[1] * join_pos[1]), num_cells[0]+num_cells[1]]
# print JOIN_ID

hwyx = [HWY75[0][0]]
hwyy = [HWY75[0][1]]
for i in range(3):
    x = np.linspace(HWY75[i][0], HWY75[i+1][0], num_cells[i], endpoint=True)
    hwyx.extend([n for n in x[1:]])
    y = np.linspace(HWY75[i][1], HWY75[i+1][1], num_cells[i], endpoint=True)
    hwyy.extend([n for n in y[1:]])
    
hwy = [(hwyx[i], hwyy[i])for i in range(len(hwyx))]


# plt.scatter([hwy[i][0] for i in range(len(hwy))], [hwy[i][1] for i in range(len(hwy))])
# plt.show()

s_num_cells = []
for i in range(len(JOIN_ID)):
    id = JOIN_ID[i]
    x = hwyx[id]
    y = hwyy[id]
    xs = SUB_RD[i][0]
    ys = SUB_RD[i][1]
    dist_sub = math.sqrt((xs - x)**2 + (ys - y)**2)
    s_num_cells.append(int(dist_sub/CELL_SIZE + 0.5))

x = np.linspace(SUB_RD[0][0], hwyx[JOIN_ID[0]], s_num_cells[0], endpoint=True)
y = np.linspace(SUB_RD[0][1], hwyy[JOIN_ID[0]], s_num_cells[0], endpoint=True)
S1 = [(x[i], y[i]) for i in range(s_num_cells[0]-1)]

x = np.linspace(SUB_RD[1][0], hwyx[JOIN_ID[1]], s_num_cells[1], endpoint=True)
y = np.linspace(SUB_RD[1][1],  hwyy[JOIN_ID[1]], s_num_cells[1], endpoint=True)
S2 = [(x[i], y[i]) for i in range(s_num_cells[1]-1)]

x = np.linspace(hwyx[JOIN_ID[2]], SUB_RD[2][0], s_num_cells[2], endpoint=True)
y = np.linspace(hwyy[JOIN_ID[2]], SUB_RD[2][1],  s_num_cells[2], endpoint=True)
S3 = [(x[i], y[i]) for i in range(s_num_cells[2])[1:]]

# print HWY75
# print SUB_RD
# print S3[-1]

MAPS = [hwy, S1, S2, S3]