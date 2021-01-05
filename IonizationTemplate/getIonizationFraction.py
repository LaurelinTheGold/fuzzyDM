from matplotlib import pyplot as plt
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/IonizationTemplate/FileList/"

#Example file name: xH_filelist_CDM_tvir2e4_zeta15.txt
#make sure to write the ionization file names to a text doc
#in Boxes, "ls xH* > xH_filelist_XDM_tvirXeX_zetaXXX.txt"

#This code takes in a folder of xH filename files and graphs xH vs z

figure = plt.figure(figsize=(10, 5))
axe = plt.axes()
axe.grid(True)
axe.set_xlim(35, 5) #For all data
axe.set_xlim(20, 5) #For interesting data
axe.set_xlabel("z")
axe.set_ylabel("xH")
axe.set_title("Ionization Fraction as a Function of Redshift")

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
axe.legend()
plt.show()