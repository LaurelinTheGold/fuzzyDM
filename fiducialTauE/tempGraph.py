from matplotlib import pyplot as plt
import numpy as np
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialTauE/"

plt.rcParams.update({"text.usetex": True, "font.size": 20})


figure = plt.figure(figsize=(10, 6)) #wide boi
axe = plt.axes()
axe.grid(True)
axe.set_xlim(5, 35) #For all data
# axe.set_xlim(5, 20) #For interesting data
axe.set_xlabel(r'$z$')
axe.set_ylabel(r'$\langle x_{\mathrm{i}}(1+\delta_{\rho}) \rangle$')
# axe.set_title("Neutral Hydrogen Fraction as a Function of Redshift")

name = glob(path2 + "*DM_x_i*")
for file in name: #foreach file matching name in directory
	z = []
	xH = []
	fileData = open(file, 'r') #opens the file
	for j in range(91): #grabs the data
		temp = fileData.readline()
		z.append(float(temp[1:6]))
		xH.append(float(temp[8:]))
	#graphy boi with labels
	plt.plot(z, xH, marker='o', markersize=4, linestyle='none')
	

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4) #taken from stackoverflow, removes duplicate labels
plt.show()
# plt.savefig("/Users/richardchen/Desktop/summerResearch/2020summer/fiducialIon/completeIon5.pdf") #save

