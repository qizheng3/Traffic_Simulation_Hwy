import matplotlib.pyplot as plt
import math


def dist_2pt(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def base_map_plotter(basemap):
    plt.figure (figsize=(8, 8))
    axes = plt.gca ()
    axes.set_xlim ([-500, 3750])
    axes.set_ylim ([-500, 3750])
    plt.grid (True)
    for i in range (len(basemap)):
        plt.scatter (*zip(*basemap[i]), s=2)
    
    # plt.scatter ([10, 50], [10, 50], s=5, c='r', marker=(5, 2))  # for checking scales
    plt.show ()