import numpy as np
import utility


def init():
    global CELL_SIZE
    global JOIN_ID
    global HWY75
    global SUB_HWY
    global TRAFFIC
    global MAPS
    global UI_BASEMAP
    global N_LANES
    
    scale = 5.5
    origin = (622, 861)
    join_pos = [1, 0.33, 0]
    traffic_lane = [985, 910]
    N_LANES = 5
    lane_offset = [-35, -25]
    # exit_offset = [20, 0]
    exit_offset = [15, 0]

    CELL_SIZE = 10
    HWY75 = [(1144, 917), (1077, 695), (734, 339), (551, 219)]
    SUB_HWY = [(1184, 918), (1239, 690), (631, 160)]

    x0 = origin[0]
    y0 = origin[1]
    HWY75 = [((x - x0) * scale, (-y + y0) * scale) for (x, y) in HWY75]
    SUB_HWY = [((x - x0) * scale, (-y + y0) * scale) for (x, y) in SUB_HWY]
    
    # print HWY75 # Now HWY75 = [(3027.6, -324.8), (2639.0, 962.8), (649.6, 3027.6), (-411.8, 3723.6)]
    
    section_lengths = [utility.dist_2pt(HWY75[i+1], HWY75[i]) for i in range(len(HWY75) - 1)]
    # print section_lengths
    
    cell_nums = [int(l / CELL_SIZE + 0.5) for l in section_lengths]
    # print cell_nums
    
    JOIN_ID = [cell_nums[0], cell_nums[0] + int (cell_nums[1] * join_pos[1]), cell_nums[0] + cell_nums[1]]
    print JOIN_ID
    
    hwyx = [HWY75[0][0]]
    hwyy = [HWY75[0][1]]
    for i in range (3):
        x = np.linspace (HWY75[i][0], HWY75[i + 1][0], cell_nums[i], endpoint=True)
        hwyx.extend ([n for n in x[1:]])
        y = np.linspace (HWY75[i][1], HWY75[i + 1][1], cell_nums[i], endpoint=True)
        hwyy.extend ([n for n in y[1:]])
    hwy = zip(hwyx, hwyy)

    join_pts = [hwy[id] for id in JOIN_ID]
    s_cell_nums = [int(utility.dist_2pt(pt1, pt2)/CELL_SIZE + 0.5) for (pt1, pt2) in zip(join_pts, SUB_HWY)]
    # print s_cell_nums
    # print join_pts
    # print SUB_HWY
    
    jx, jy = zip(*join_pts)
    sx, sy = zip(*SUB_HWY)

    MAPS = [hwy]
    
    dx = exit_offset[0]
    dy = exit_offset[1]
    
    for i in range(2):
        x = np.linspace (sx[i] + dx, jx[i] + dx, s_cell_nums[i], endpoint=True)
        y = np.linspace (sy[i] + dy, jy[i] + dy, s_cell_nums[i], endpoint=True)
        join_hwy = zip(x, y)[:-1]
        MAPS.append(join_hwy)

    x = np.linspace (jx[2] + dx, sx[2] + dx, s_cell_nums[2], endpoint=True)
    y = np.linspace (jy[2] + dy, sy[2] + dy, s_cell_nums[2], endpoint=True)
    MAPS.append(zip(x, y)[1:])

    UI_BASEMAP = []
    for i in range(N_LANES-1):
        UI_BASEMAP.append([(x + lane_offset[0] * (i+1), y + lane_offset[1] * (i+1)) for (x, y) in MAPS[0]])
    
    UI_BASEMAP.reverse()
    UI_BASEMAP.extend(MAPS)
