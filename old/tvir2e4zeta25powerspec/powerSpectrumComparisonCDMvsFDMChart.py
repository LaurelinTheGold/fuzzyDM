import struct as s
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from matplotlib.animation import FuncAnimation
from matplotlib import animation

#NB make sure there is a slash at the end of the dir
#adjust paths for non template use
path = "/Users/richardchen/Desktop/summerResearch/2020summer/tvir2e4zeta25powerspec/cdmPowerSpectra/"
path3 = "/Users/richardchen/Desktop/summerResearch/2020summer/tvir2e4zeta25powerspec/fdmPowerSpectra/"

fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
plt.xlabel("k (Mpc-1)")
plt.ylabel("Delta$^2$ {21}(k)")
plt.title("Power Spectrum Evolution at Various Redshifts, Pober CDM")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.02, 4)
ax.set_ylim(0.001, 1500)
ax.grid(True)

def open_data(data, d):
    k = []
    PS = []
    dataopen = open(data, 'r')
    x = 0
    for i in range(d):
        x = dataopen.readline()
        k.append(float(x.split()[0]))
        PS.append(float(x.split()[1]))
    return(k, PS)

redshiftsToGraph = [600, 900, 1300]
for i in redshiftsToGraph:
    s = str(i)
    if (len(s) == 3):
        s = "0" + s
    # print(s)
    s = s[:-2] + '.' + s[-2:]
    # print(s) 
    cdmData = open_data("".join(glob(path + "*z0" + s + "*")), 13)
    fdmData = open_data("".join(glob(path3 + "*z0" + s + "*")), 13)
    xCDM = cdmData[0]
    yCDM = cdmData[1]
    xFDM = fdmData[0]
    yFDM = fdmData[1]
    temp = plt.plot(xCDM, yCDM, label=("CDM, z=" + s), marker='o', markersize=6)
    plt.plot(xFDM, yFDM, label=("FDM, z=" + s), marker='*', markersize=7, color=temp[0].get_color())


ax.legend()
plt.show()


