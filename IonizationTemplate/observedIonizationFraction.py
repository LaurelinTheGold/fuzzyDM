from matplotlib import pyplot as plt
import numpy as np
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/IonizationTemplate/FileList/"

#Example file name: xH_filelist_CDM_tvir2e4_zeta15.txt
#make sure to write the ionization file names to a text doc
#in Boxes, "ls xH* > xH_filelist_XDM_tvirXeX_zetaXXX.txt"

plt.rcParams.update({"text.usetex": True})

#This code takes in a folder of xH filename files and graphs xH vs z

figure = plt.figure(figsize=(10, 5)) #wide boi
# figure = plt.figure() #default narrow boi
axe = plt.axes()
axe.grid(True)
axe.set_xlim(5, 35) #For all data
axe.set_xlim(5, 20) #For interesting data
axe.set_xlabel(r'$z$')
axe.set_ylabel(r'$\langle x_{HI} \rangle$')
# axe.set_title("Neutral Hydrogen Fraction as a Function of Redshift")

name = glob(path2 + "xH*")
for file in name: #foreach file matching name in directory
	fileName = file.split("/")[-1] #gets filename from full path
	parsedFileName = fileName.split("_") #parse based on separator
	if (parsedFileName[1] == "filelist"): #follows proper naming convention
		dm = parsedFileName[2] #CDM/FDM
		tvir = parsedFileName[3] #Tvir
		zetaList = parsedFileName[4].rpartition('.') #Checks for .txt on end
		if (zetaList[-1] == "txt"): #remove if present
			zeta = zetaList[0]
		else: #else ignore
			zeta = parsedFileName[4]
		z = []
		xH = []
		fileData = open(file, 'r') #opens the file
		for j in range(83): #grabs the data
			temp = fileData.readline()
			z.append(float(temp[13:18]))
			xH.append(float(temp[21:29]))
		#graphy boi with labels
		plt.plot(z, xH, label=(dm+": "+"Tvir = "+tvir[4:]+", Zeta = "+zeta[4:]), marker='o', markersize=3, linestyle='none')
	if (parsedFileName[1] == "observed.txt"): #fixed points from papers
		fileData = open(file, 'r')
		colorMap = {}
		while (True):
			line = fileData.readline()
			if (line == ''):
				break
			dataList = line.split(" ") #parse line by spaces
			author = dataList[5].strip() #strips newlines off the author name
			year = dataList[6].strip()
			floatData = [None] * 5 #data size z xH, +error, -error, xerror 
			for index in range(5):
				floatData[index] = float(dataList[index]) #parses float from string
			yErr = np.array([[floatData[3], floatData[2]]]).T #tranposes the array cuz errorbar is a finicky piece of shit
			if colorMap.__contains__(author):
				#checks if datapoint or if upper/lower bound
				plt.errorbar(floatData[0], floatData[1], yerr=yErr, xerr=floatData[4], label=author+"+"+year[-2:],
				fmt=('x-' if (floatData[2] == 0 or floatData[3] == 0) else '-o'), color=colorMap.get(author)[0].get_color())
			else:
				temp = plt.errorbar(floatData[0], floatData[1], yerr=yErr, xerr=floatData[4], 
				fmt=('x-' if (floatData[2] == 0 or floatData[3] == 0) else '-o'), label=author+"+"+year[-2:])
				colorMap[author] = temp

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4) #taken from stackoverflow, removes duplicate labels
plt.show()
# plt.savefig("/Users/richardchen/Desktop/summerResearch/2020summer/IonizationTemplate/completeIon.pdf") #save