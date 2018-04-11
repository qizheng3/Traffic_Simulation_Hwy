import matplotlib.pyplot as plt
import math


def dist_2pt(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def base_map_plotter(basemap):
    plt.figure (1, figsize=(8, 8))
    axes = plt.gca ()
    axes.set_xlim ([-500, 3750])
    axes.set_ylim ([-500, 3750])
    plt.grid (True)
    for rd in basemap:
        plt.scatter (*zip(*rd), s=2)
    
    # plt.scatter ([10, 50], [10, 50], s=5, c='r', marker=(5, 2))  # for checking scales
    plt.show ()
 
    
def realtime_plotter(lanes):
    plt.figure (2, figsize=(8, 8))
    axes = plt.gca ()
    axes.set_xlim ([-500, 3750])
    axes.set_ylim ([-500, 3750])
    plt.grid (True)
    X = []
    Y = []
    for lane in lanes:
        for c in lane.cells:
            if c.veh is not None:
                X.append(c.x)
                Y.append(c.y)
    plt.scatter(X, Y, s=1)
    plt.show(block=False)
