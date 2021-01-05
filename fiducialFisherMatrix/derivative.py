import matplotlib.pyplot as plt
from glob import glob
import sys

#should be called as $python3 derivative.py (subdirectory name)
masterPath = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/baseFDM/"
incompletePath = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/"
folderName = sys.argv[1] #specify folder in terminal when calling script
numWavenumbers = 13 
dx = 0.05

completePath = incompletePath + folderName #full pathname
if (completePath[-1] != "/"): #appends "/" if I forgot to
	completePath = completePath + "/"

difQuant = folderName.replace('_', "")

#find corresponding z files for each z in original
tsList = glob(masterPath + "ps_nov_no_halos_z0*")
for file in tsList:
	# print(file)
	fileName = file.split("/")[-1] #gets filename from full path
	parsedFileName = fileName.split("_") #parse based on separator
	z = parsedFileName[4][2:] #redshift of that file
	#find corresponding file 
	targetFile = glob(completePath + "ps_nov_no_halos_z0" + z + "*") #should be singleton list
	#open both
	fiducialFileData = open(file, 'rb')
	fisherFileData = open(targetFile[0], 'rb')
	#open outputfilewriter
	outputFile = open("derivOutput/fisher_derivative_"+difQuant+"_z0"+z+".txt", "w")
	#for each k
	for i in range(numWavenumbers):
		#check that k for both is the same
		line_fiducial = fiducialFileData.readline()
		line_fisher = fisherFileData.readline()
		k_fiducial = float(line_fiducial.split()[0])
		k_fisher = float(line_fisher.split()[0])
		if k_fisher == k_fiducial:
			#Using derivative as f(x+dx) - f(x) / dx, find dx based on the changed parameter. 
			ps_fiducial = float(line_fiducial.split()[1])
			ps_fisher = float(line_fisher.split()[1])
			diffPrime =ps_fisher - ps_fiducial
			differential = diffPrime / dx
			#write k, d/dQ ps(k) to file 
			outputFile.write(str(k_fiducial)+" "+str(differential)+"\n")
		else:
			outputFile.write("Error\n")
	outputFile.close()

#zetaX 2e56 -> 2.1e56, mFDM 1e-21 -> 1.05e-21, fstar 0.05 -> 0.0525
#zetaX 1e55, mFDM 5e-23, fstar 0.0025
#Names: f_star, m_FDM, zeta_X
# zetaX_differential = 1.0e55
# fStar_differential = 0.0025
# mFDM_differential = 5.0e-23
# if completePath.split("/")[-2] == "f_star":
# 	# dx = fStar_differential
# 	difQuant = "fStar"
# elif completePath.split("/")[-2] == "m_FDM":
# 	# dx = mFDM_differential
# 	difQuant = "mFDM"
# elif completePath.split("/")[-2] == "zeta_X":
# 	# dx = zetaX_differential
# 	difQuant = "zetaX"
# else:
# 	raise NotADirectoryError("Not a Directory")
# 	exit(1)