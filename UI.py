from Tkinter import *
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import Queue
import threading
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
    
    def processData(self, highway):
        return arange(0.0, 3, 0.1), sin(2 * pi * arange(0.0, 3, 0.1) + highway)

    def processMessage(self):
        self.root.after(500, self.processMessage) # check message queue every 0.5s
        while not self.messageQueue.empty():
            x, y = self.messageQueue.get()
            self.figure.clf()
            self.figure.add_subplot(111).scatter(x, y, s = 3, color = 'r')
            self.canvas.show()
            break
            
    
    def drawFrame(self, highway):
        x, y = self.processData(highway)
        self.messageQueue.put((x, y))
      
    def display(self, highway):
        pass

        
        
    def mainloop(self):
        self.root.mainloop()
        

if __name__ == '__main__':
    UI = UI()
    for highway in range(10):
        pass
    UI.mainloop()
