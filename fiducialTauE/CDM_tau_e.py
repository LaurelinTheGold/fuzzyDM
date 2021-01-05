from glob import glob
from decimal import *
import math

# leadCoeff = Decimal('1.868E-3')
# zEnd = Decimal('5.0')
# omegaM = Decimal('0.308')
# omegaLambda = Decimal('1.0') - omegaM

leadCoeff = 1.868E-3
zEnd = 5.0
omegaM = 0.308
omegaLambda = 1.0 - omegaM


numDataPoints = 91

# postReion = Decimal('2.0')/(3*omegaM)*((omegaM*((1+zEnd)**3)+omegaLambda).sqrt()-1)
postReion = 2.0/(3*omegaM)*(math.sqrt(omegaM*((1+zEnd)**3)+omegaLambda)-1)

def integrand(zPrimePlusOne, boi): 
	return (zPrimePlusOne**2)*boi/math.sqrt(omegaM*(zPrimePlusOne**3)+omegaLambda)

#make sure that these are filled with decimals truncated to 15 places
z = []
oldData = []
#import the data from file
path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialTauE/CDM_x_i_one_plus_delta.txt"
fileData = open(path2, 'r') #opens the file
for j in range(91): #grabs the data
	temp = fileData.readline()
	z.append(float(temp[1:6]))
	oldData.append(float(temp[8:16]))
	print(temp[8:16])

#Process oldData to get the integrand
data = [None]*numDataPoints
for i in range(numDataPoints):
	print(i)
	data[i] = integrand(1+z[i], oldData[i])

# reion = Decimal('0')
reion = 0.0
for i in range(numDataPoints-1):
	reion += 0.5*(data[i]+data[i+1])*(z[i+1]-z[i]) #trapezoid rule

tauE = leadCoeff * (postReion + reion)

print(tauE)

#0.06745474603087383
#0.0675 for CDM