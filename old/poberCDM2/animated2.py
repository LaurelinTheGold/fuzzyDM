import struct as s
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from matplotlib.animation import FuncAnimation
from matplotlib import animation

path = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM2/powerSpectra/"
path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM2/"
path3 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM/powerSpectra/"
path4 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM/"

redshiftArr = [3451, 3381, 3313, 3246, 3181, 3116, 3053, 2991, 2931, 2871, 2813, 2756, 2700, 2645, 2591, 2538, 2487, 2436, 2386, 2338, 2290, 2243, 2197, 2152, 2108, 2064, 2022, 1980, 1940, 1900, 1860, 1822, 1784, 1747, 1711, 1676, 1641, 1607, 1573, 1540, 1508, 1477, 1446, 1415, 1386, 1357, 1328, 1300, 1273, 1246, 1219, 1193, 1168, 1143, 1119, 1095, 1071, 1049, 1026, 1004, 982, 961, 940, 920, 900, 880, 861, 842, 824, 806, 788, 770, 753, 737, 720, 704, 688, 673, 658, 643, 628, 614, 600]

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
        psDic["ps_{0}".format(i)] = open_data("".join(glob(filepath)), 13)
        psDic2["ps_{0}".format(i)] = open_data("".join(glob(filepath2)), 13)
    line.set_data([], [])
    line3.set_data([], [])
    return line

fig = plt.figure(figsize = (24, 16))
ax = plt.axes()
plt.xlabel("k (Mpc-1)")
plt.ylabel("Delta$^2$ {21}(k)")
plt.title("Power Spectrum Evolution at Various Redshifts, Pober CDM")

line4, = ax.plot([], [])
line, = ax.plot([], [], lw=3)
line3, = ax.plot([], [], lw=3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.01, 4)
ax.set_ylim(0.000002, 1100)
ax.grid(True)

zRed = []
xH = []
zRed2 = []
xH2 = []
filedata = open("".join(glob(path2 + "filenames.txt")), 'r')
filedata2 = open("".join(glob(path4 + "filenames.txt")), 'r')

for i in range(83):
    temp = filedata.readline()
    temp2 = filedata2.readline()
    zRed.append(float(temp[13:18]))
    xH.append(float(temp[21:29]))
    zRed2.append(float(temp2[13:18]))
    xH2.append(float(temp2[21:29]))

#this is because the file is listed in reversed redshift order
xH.reverse()
xH2.reverse()

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
    line.set_label("xH = " + str(xH[i]) + " (T_s >> T_k)")
    line3.set_label("xH = " + str(xH2[i]))
    ax.legend(loc = 2)
    return 

anim = FuncAnimation(fig, animate, init_func=init, frames=83, interval=1, blit=False)
# plt.show()
anim.save('psAtDiffZrunComparrison.mp4', fps=15)
