# from config import *
#
# global CELL_SIZE
# global HYW75
#
# hwys = []

import matplotlib.pyplot as plt


L1 = [(2747,0), (2478, 914), (602, 2866), (0, 3253)]
xx =[x*1.05 for (x, _) in L1]
yy =[y*1.05 for (_, y) in L1]

print xx, yy

plt.plot(xx, yy)
plt.show()

print(L1)
num = [0]*3
for i in range(1, len(L1)):
  x0, y0 = L1[i]
  x1, y1 = L1[i-1]
  num[i-1] = int (((x1-x0)**2 + (y1-y0)**2)**0.5 / 20 + 0.5)
  print('(', x0,',', y0, ')', '(', x1,',', y1, ')', num[i-1])
