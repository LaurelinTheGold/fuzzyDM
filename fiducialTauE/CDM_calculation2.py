import array
from glob import glob
from decimal import *
# import numpy as np

#constants and other fixed things
boxLength = 256;
volume = boxLength*boxLength*boxLength;
numRedshifts = 91
path = "/home/laurelin/Desktop/21cmFAST_CDM_Tvir2e4_zeta20/Temp/";
outputFile = open(r"outputDecimal.txt", "w")

z = []

#Redshift List
name = glob(path + "names.txt")
for file in name:
	fileData = open(file, 'r') #opens the file
	for j in range(numRedshifts): #grabs the data
		temp = fileData.readline()
		z.append(temp.split("_")[3][1:])
z.sort()

#For each redshift, find corresponding files
for redshift in z:
	print(redshift)
	neutralFractionList = glob(path + "xH_nohalos_z" + redshift + "*")
	densityList = glob(path + "updated_smoothed_deltax_z" + redshift + "*")
	# print(neutralFractionList)
	# print(densityList)
	neutralFrac = neutralFractionList[0]
	density = densityList[0]
	#Do the thing
	xHData = open(neutralFrac, 'rb')
	denData = open(density, 'rb')

	xHArr = array.array('f')
	densArr = array.array('f')
	xHArr.fromfile(xHData, volume)
	densArr.fromfile(denData, volume)

	# total = Decimal('0');
	total = 0.0;
	for i in range(volume):
		# total += (Decimal('1') - Decimal(format(Decimal.from_float(xHArr[i]), '.15G')) * Decimal(format(Decimal.from_float(densArr[i]), '.15G')))
		total += (1-xHArr[i])*(1+densArr[i])
	# outputFile.write(redshift + " " + str(total / Decimal(str(volume))) + "\n")
	outputFile.write(redshift + ", " + str(total/volume) + "\n")
	# outputFile.write(redshift + ", " + format(str(total/volume), '.6G') + "\n")
outputFile.close()