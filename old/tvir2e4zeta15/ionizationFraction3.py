from matplotlib import pyplot as plt
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/tvir2e4zeta15/"

# ALL CDM
# #filenames.txt: Tvir 2e4, zeta 15
# #filenames2.txt: Tvir 1e4, zeta 30
# #filenames3.txt: Tvir2e4, zeta 20
# #filenames4.txt: Tvir 2e4, zeta 25

# figu = plt.figure(figsize=(24, 16));
figu = plt.figure();
axe = plt.axes()
axe.grid(True)
axe.set_xlim(35, 5)
# axe.set_xlim(20, 5)
axe.set_xlabel("z")
axe.set_ylabel("xH")
axe.set_title("Ionization Fraction as a Function of Redshift")

fileList = ["filenames.txt", "filenames2.txt", "filenames3.txt", "filenames4.txt"]
labelList = ["Tvir = 2e4, zeta = 15", "Tvir = 1e4, zeta = 30", "Tvir = 2e4, zeta = 20", "Tvir = 2e4, zeta = 25"]

# for i in fileList:
for i in range(4):
	# print(i)
	zRed = []
	xH = []
	filedata = open("".join(glob(path2 + fileList[i])), 'r')
	for j in range(83):
		temp = filedata.readline()
		zRed.append(float(temp[13:18]))
		xH.append(float(temp[21:29]))
	plt.scatter(zRed, xH, label=labelList[i])

axe.legend()

plt.show()