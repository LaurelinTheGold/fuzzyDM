import matplotlib.pyplot as plt
from glob import glob
import sys

#should be called as $python3 derivative.py (subdirectory name)
masterPath1 = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/" # base_fdm, 1.05
incompletePath = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/twoSideDeriv/" #0.95
folderName = sys.argv[1] #specify folder in terminal when calling script
numWavenumbers = 13 
dx = 0.05

#NB master and complete paths flipped from fiducial fisher where master was 1 and fisher was 1.05
# Now, master is 1.05 and complete is 0.95

# One sided: F(p + 0.05p) - F(p) / .05p where dx = 0.05p = 
# Two sided Deriv: F(.95p + .1p (=1.05p)) - F(.95p) / .1p but scale x = .95p, dx = .1p = 2/19 x
#                  F(x + dx) - F(x) / dx
# Treat it like one sided deriv with .95p as the base value. this makes dx 0.1052631579
dx = 0.1052631579 #wrong
dx = 0.1

completePath = incompletePath + folderName #full pathname
if (completePath[-1] != "/"): #appends "/" if I forgot to
	completePath = completePath + "/"

#seperate base models at.95 * param necessitates seperate parsing
masterPath = masterPath1 + folderName #full pathname
if (masterPath[-1] != "/"): #appends "/" if I forgot to
	masterPath = masterPath + "/"

difQuant = folderName.replace('_', "") #makes more readable by removing underscores for prototype print. 

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
			diffPrime = ps_fiducial - ps_fisher
			differential = diffPrime / dx
			#write k, d/dQ ps(k) to file 
			outputFile.write(str(k_fiducial)+" "+str(differential)+"\n")
		else:
			outputFile.write("Error\n")
	outputFile.close()
