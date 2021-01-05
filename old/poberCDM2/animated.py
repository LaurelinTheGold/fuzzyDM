import struct as s
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from matplotlib.animation import FuncAnimation
from matplotlib import animation

path = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM2/powerSpectra/"
path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM2/"
# I copied all the power spectrum files from folio into the above

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

# def make_ps_plot(powerspec, DM, title, line):
#     plt.loglog(powerspec[0], powerspec[1], label = DM, linestyle = line)
#     plt.xlabel("k (Mpc-1)")
#     plt.ylabel("Delta$^2$ {21}(k)")
#     plt.title(title)
#     plt.legend(loc = 0)

redshiftArr = [3451, 3381, 3313, 3246, 3181, 3116, 3053, 2991, 2931, 2871, 2813, 2756, 2700, 2645, 2591, 2538, 2487, 2436, 2386, 2338, 2290, 2243, 2197, 2152, 2108, 2064, 2022, 1980, 1940, 1900, 1860, 1822, 1784, 1747, 1711, 1676, 1641, 1607, 1573, 1540, 1508, 1477, 1446, 1415, 1386, 1357, 1328, 1300, 1273, 1246, 1219, 1193, 1168, 1143, 1119, 1095, 1071, 1049, 1026, 1004, 982, 961, 940, 920, 900, 880, 861, 842, 824, 806, 788, 770, 753, 737, 720, 704, 688, 673, 658, 643, 628, 614, 600]

psDic = {}
def init():
    for i in redshiftArr:
        s = str(i)
        s2 = s[:-2] + '.' + s[-2:]
        if (len(s2) == 4):
            s2 = '0' + s2
        path2 = path + "ps*z0"+ s2 + "*"
        psDic["ps_{0}".format(i)] = open_data("".join(glob(path2)), 13)
    line.set_data([], [])
    return line

# Animaty boi?
fig = plt.figure(figsize = (24, 16))
ax = plt.axes()
plt.xlabel("k (Mpc-1)")
plt.ylabel("Delta$^2$ {21}(k)")
plt.title("Power Spectrum Evolution at Various Redshifts, Pober CDM")
# plt.legend(loc = 2)

line, = ax.plot([], [], lw=3)
line2, = ax.plot([], [])
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.01, 4)
ax.set_ylim(0.000002, 1100)
ax.grid(True)

zRed = []
xH = []
filedata = open("".join(glob(path2 + "filenames.txt")), 'r')
for i in range(83):
    temp = filedata.readline()
    zRed.append(float(temp[13:18]))
    xH.append(float(temp[21:29]))
    # print(i)
    # print(float(temp.split()[0]))
# figu = plt.figure(figsize=(24, 16));
# axe = plt.axes()
# axe.grid(True)
# axe.set_xlim(35, 5)
# axe.set_xscale("log")
# # axe.set_yscale("log")
# plt.plot(zRed, xH, '-')
# plt.show()

#this is because the file is listed in reversed redshift order
xH.reverse()

def animate(i):
    x = psDic["ps_" + str(redshiftArr[i])][0]
    y = psDic["ps_" + str(redshiftArr[i])][1]
    line.set_data(x, y)
    # line2.set_data(x, y)
    j = str(redshiftArr[i])
    u = "z = " + j[:-2] + '.' + j[-2:]
    line.set_label(u)
    line2.set_label("xH = " + str(xH[i]))
    # line.set_label(i)
    ax.legend(loc = 2)
    return line, line2

anim = FuncAnimation(fig, animate, init_func=init, frames=83, interval=1, blit=False)
# plt.show()
anim.save('psAtDiffZ2.mp4', fps=15)
