from matplotlib import pyplot as plt
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM/"

zRed = []
xH = []
filedata = open("".join(glob(path2 + "filenames.txt")), 'r')
for i in range(83):
    temp = filedata.readline()
    zRed.append(float(temp.split()[0]))
    xH.append(float(temp.split()[1]))
    # print(i)
for i in range(83):
    print(zRed[i], xH[i])
# figu = plt.figure(figsize=(24, 16));
# axe = plt.axes()
# axe.grid(True)
# axe.set_xlim(35, 5)
# axe.set_xlabel("z")
# axe.set_ylabel("xH")
# plt.scatter(zRed, xH)
# plt.show()