import math
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Tkinter import *

import Queue
import warnings

from numpy import arange, sin, pi
from time import sleep

class UI(object):
    # UI config
    programTitle = "Traffic Simulation Software Version 1.0"
    animationSize = (12, 3)
    animationDpi = 100
    refreshInterval = 500 # refresh frame interval in milli-second
    
    def __init__(self):
        # UI preparation
        warnings.filterwarnings("ignore") # ignore warnings
        plt.use('TKAgg') # use matplotlib in Tkinter
        self.root = Tk()
        self.root.resizable(False, False) # disable window size change
        self.root.title(self.programTitle) # program title
        
        # draw matplotlib output to Tkinter
        self.figure = Figure(figsize = (self.animationSize[0], self.animationSize[1]), dpi = self.animationDpi) # set figure
        self.canvas = FigureCanvasTkAgg(self.figure, master = self.root) # TODO: subject to change root to frame
        self.canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 1) # TODO: subject to change canvas position
        
        # set window in the center of the screen
        # ===== quote http://www.jb51.net/article/61962.htm =====
        self.root.update() # update window (must do)
        curWidth = self.root.winfo_reqwidth() # get current width
        curHeight = self.root.winfo_height() # get current height
        scnWidth,scnHeight = self.root.maxsize() # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight, (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmpcnf)
        # ===== end quote =====
        
        # set message queue
        self.messageQueue = Queue.Queue()
        self.processMessage()
        
    def processData(self, highways):
        x = []
        y = []
        xx = []
        yy = []
        argR = 0.2
        argL = 0.3
        
        hwy = highways.RL
        length = len(hwy.lanes[0].cells)
        for i, lane in enumerate(hwy.lanes[:-1]):
            for j, cell in enumerate(lane.cells):
                if cell is not None:
                    x.append(20 + i*30)
                    y.append(j*5)
        x0 = i * 30 + 25
        y0 = length / 2 * 5

        for k, cell in enumerate(hwy.lanes[-1].cells):
            if cell is not None:
                dist = k * 5
                x.append(dist * math.sin(argR) + x0)
                y.append(dist * math.cos(argR) + y0)

        hwyL = highways.LL
        for i, lane in enumerate(hwyL.lanes[:-1]):
            for j, cell in enumerate(lane.cells):
                if cell is not None:
                    xx.append(-20 - i*30)
                    yy.append(length*5 - j*5)
                    
        x0 = - i*30 - 25
        y0 = length * 5 * 0.8

        for k, cell in enumerate(hwy.lanes[-1].cells):
            if cell is not None:
                dist = k * 5
                xx.append(- dist * math.sin(argL) + x0)
                yy.append(- dist * math.cos(argL) + y0)
               
        return x, y, xx, yy

    def drawFrame(self, x, y, xx, yy):
        self.figure.clf()
        self.figure.add_subplot(111).scatter(y, x, s = 0.5, color='b')
        self.figure.add_subplot(111).scatter(yy, xx, s=0.5, color='r')
        axes = self.figure.gca()
        axes.set_ylim ([-700, 400])
        axes.set_xlim([0, 3000])
        self.canvas.show()

    def processMessage(self):
        self.root.after(self.refreshInterval, self.processMessage) # check message queue every interval
        while not self.messageQueue.empty():
            x, y, xx, yy = self.messageQueue.get()
            self.drawFrame(x, y, xx, yy)
            break        

    def display(self, highways):
        x, y, xx, yy = self.processData(highways)
        self.messageQueue.put((x, y, xx, yy))
        
    def mainloop(self):
        self.root.mainloop()
