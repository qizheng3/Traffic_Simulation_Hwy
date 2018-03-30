from Tkinter import *
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import warnings

from numpy import arange, sin, pi
from time import sleep

class UI(object):
    # UI config
    programTitle = "Traffic Simulation Software Version 1.0"
    animationSize = (5, 4)
    animationDpi = 100
    
    def __init__(self):
        # UI preparation
        warnings.filterwarnings("ignore") # ignore warnings
        plt.use('TKAgg') # use matplotlib in Tkinter
        self.root = Tk()
        self.root.resizable(False, False) # disable window size change
        self.root.title(self.programTitle) # program title
        
        # draw matplotlib output to Tkinter
        self.figure = Figure(figsize = (self.animationSize[0], self.animationSize[1]), dpi = self.animationDpi)# set figure
        self.canvas = FigureCanvasTkAgg(self.figure, master = self.root) # TODO: subject to change root to frame
        self.canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 1) # TODO: subject to change canvas position
    
    def processData(self,i):
        self.t = arange(0.0, 3, 0.01)
        self.s = sin(2 * pi * self.t + i)

    def drawFrame(self,i):
        self.processData(i)
        self.figure.clf()
        self.figure.add_subplot(111).plot(self.t, self.s)
        self.canvas.show()
    
    def display(self):
        # set window in the center of the screen
        # =====http://www.jb51.net/article/61962.htm=====
        self.root.update() # update window (must do)
        curWidth = self.root.winfo_reqwidth() # get current width
        curHeight = self.root.winfo_height() # get current height
        scnWidth,scnHeight = self.root.maxsize() # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight, (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmpcnf)
        #==========
        
        # run animation
        for i in range(10):
            self.drawFrame(i)
        
        # main loop
        self.root.mainloop()

UI().display()
