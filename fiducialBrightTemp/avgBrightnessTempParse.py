from matplotlib import pyplot as plt
import numpy as np
from glob import glob

path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialBrightTemp/FileList/"

outputFile = open(r"parsedAvgBrightTemp.txt", "w")

name = glob(path2 + "avgBrightTemp_*")
for file in name: #foreach file matching name in directory
	fileData = open(file, 'r') #opens the file
	for j in range(91): #grabs the data
		temp = fileData.readline()
		lineList = temp.split("_")
		getZ = float(lineList[4][1:])
		getABT = float(lineList[10][5:])
		outputFile.write(str(getZ) + " " + str(getABT) + "\n")
