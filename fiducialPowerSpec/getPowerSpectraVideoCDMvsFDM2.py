import struct as s
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from matplotlib.animation import FuncAnimation
from matplotlib import animation

#NB make sure there is a slash at the end of the dir
#adjust paths for non template use
path = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialPowerSpec/cdmPowerSpectra/"
path3 = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialPowerSpec/fdmPowerSpectra/"

redshiftArr = []
name = glob(path + "*")
for file in name:
    fileName = file.split("/")[-1]
    parsedFileName = fileName.split("_")
    redshift = round(float(parsedFileName[4][1:])*100)
    redshiftArr.append(redshift)
redshiftArr.sort()
redshiftArr.reverse()
# print(redshiftArr)


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

psDic = {}
psDic2 = {}
def init():
    for i in redshiftArr:
        s = str(i)
        s2 = s[:-2] + '.' + s[-2:]
        if (len(s2) == 4):
            s2 = '0' + s2
        filepath = path + "ps*z0" + s2 + "*"
        filepath2 = path3 + "ps*z0" + s2 + "*"
        # print(filepath)
        # print(filepath2)
        psDic["ps_{0}".format(i)] = open_data("".join(glob(filepath)), 13)
        psDic2["ps_{0}".format(i)] = open_data("".join(glob(filepath2)), 13)
    line.set_data([], [])
    line3.set_data([], [])
    return line

fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
plt.xlabel("k (Mpc-1)")
plt.ylabel("Delta$^2$ {21}(k)")
plt.title("CDM FDM Power Spectra, z scroll, new fidicial model")

line4, = ax.plot([], [])
line, = ax.plot([], [], lw=3)
line3, = ax.plot([], [], lw=3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.02, 4)
ax.set_ylim(0.001, 1500)
ax.grid(True)


def animate(i):
    x = psDic["ps_" + str(redshiftArr[i])][0]
    x2 = psDic2["ps_" + str(redshiftArr[i])][0]
    y = psDic["ps_" + str(redshiftArr[i])][1]
    y2 = psDic2["ps_" + str(redshiftArr[i])][1]
    line.set_data(x, y)
    line3.set_data(x2, y2)
    j = str(redshiftArr[i])
    u = "z = " + j[:-2] + '.' + j[-2:]
    line4.set_label(u)
    line.set_label("CDM")
    line3.set_label("FDM")
    ax.legend(loc = 2)
    return 

anim = FuncAnimation(fig, animate, init_func=init, frames=91, interval=100, blit=False)
# plt.show()
anim.save('tvir2e4_zeta20_CDMvsFDM_comparison2.mp4', fps=15)



