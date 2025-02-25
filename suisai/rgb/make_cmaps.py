import matplotlib
import numpy as np

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#43676b','#80aba9','w',"#d8a373",'#9f563a'])
rgbtemp = cmap(np.linspace(0, 1, 512))[np.newaxis, :, :3][0]
np.savetxt('forestdawn-rgb.txt', rgbtemp)

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#9f563a',"#d8a373",'w'])
rgbtemp = cmap(np.linspace(0, 1, 512))[np.newaxis, :, :3][0]
np.savetxt('solar-rgb.txt', rgbtemp)

