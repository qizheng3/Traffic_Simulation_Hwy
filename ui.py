import math
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Tkinter import *
import settings

import Queue
import threading
import warnings

from numpy import arange, sin, pi
from time import sleep


class UI (object):
    # UI config
    programTitle = "Traffic Simulation Software Version 1.0"
    animationSize = (8, 8)
    animationDpi = 100
    refreshInterval = 500  # refresh frame interval in milli-second
    
    def __init__(self):
        # UI preparation
        warnings.filterwarnings ("ignore")  # ignore warnings
        plt.use ('TKAgg')  # use matplotlib in Tkinter
        self.root = Tk ()
        self.root.resizable (True, True)  # disable window size change
        self.root.title (self.programTitle)  # program title
        
        # draw matplotlib output to Tkinter
        self.figure = Figure (figsize=(self.animationSize[0], self.animationSize[1]),
                              dpi=self.animationDpi)  # set figure
        self.canvas = FigureCanvasTkAgg (self.figure, master=self.root)  # TODO: subject to change root to frame
        self.canvas.get_tk_widget ().grid (row=0, column=0, rowspan=1)  # TODO: subject to change canvas position
        
        # set window in the center of the screen
        # ===== quote http://www.jb51.net/article/61962.htm =====
        self.root.update ()  # update window (must do)
        curWidth = self.root.winfo_reqwidth ()  # get current width
        curHeight = self.root.winfo_height ()  # get current height
        scnWidth, scnHeight = self.root.maxsize ()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight, (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry (tmpcnf)
        # ===== end quote =====
        
        # set message queue
        self.messageQueue = Queue.Queue ()
        

    def drawFrame(self, x, y, num):
        self.figure.clf ()
        colors = ['b', 'r', 'm', "#00EEEE", "#8B2323", 'g', 'k', "#8B2323"]
        for i in range(num):
            self.figure.add_subplot (111).scatter (x[i], y[i], s=2, color=colors[i])
        axes = self.figure.gca ()
        axes.set_ylim ([-200, 3500])
        axes.set_xlim ([-300, 3500])
        self.canvas.show ()

    def processMessage(self):
        # self.root.after (self.refreshInterval, self.processMessage)  # check message queue every interval
        # while not self.messageQueue.empty ():
        #     x, y = self.messageQueue.get ()
        #     self.drawFrame (x, y)
        #     print 2
        #     break
        while True:
            if not self.messageQueue.empty ():
                x, y = self.messageQueue.get ()
                num = len(x)
                self.drawFrame (x, y, num)
                # print "*"
            # else:
            # print "$"
            sleep (1)

    def sendMessage(self, x, y):
        # x, y = self.processData (highways)
        self.messageQueue.put ((x, y))

    def mainloop(self):
        self.root.mainloop ()
