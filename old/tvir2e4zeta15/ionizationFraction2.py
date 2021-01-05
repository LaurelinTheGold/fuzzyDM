from matplotlib import pyplot as plt
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/tvir2e4zeta15/"

zRed = []
zRed2 = []
xH = []
xH2 = []
filedata = open("".join(glob(path2 + "filenames.txt")), 'r')
filedata2 = open("".join(glob(path2 + "filenames2.txt")), 'r') 
for i in range(83):
    temp = filedata.readline()
    temp2 = filedata2.readline()
    zRed.append(float(temp[13:18]))
    zRed2.append(float(temp2[13:18]))
    xH.append(float(temp[21:29]))
    xH2.append(float(temp2[21:29]))
    # print(i)
# for i in range(83):
#     print(zRed[i], xH[i])
figu = plt.figure(figsize=(24, 16));
axe = plt.axes()
axe.grid(True)
axe.set_xlim(35, 5)
axe.set_xlabel("z")
axe.set_ylabel("xH")
plt.scatter(zRed, xH, label="Tvir = 2e4, zeta = 15")
plt.scatter(zRed2, xH2, label="Tvir = 1e4, zeta = 30")
# axe.legend(loc = 2)
axe.legend()
plt.show()
#filenames.txt: Tvir 2e4, zeta 15
#filenames2.txt: Tvir 1e4, zeta 30
#filenames3.txt: Tvir2e4, zeta 20
#filenames4.txt: Tvir 2e4, zeta 25