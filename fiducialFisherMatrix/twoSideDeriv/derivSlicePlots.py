import matplotlib.pyplot as plt
from glob import glob
import sys

import matplotlib.font_manager as font_manager
import matplotlib as mpl

plt.rcParams.update({"text.usetex": True, "font.size": 20})

plt.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + '/fonts/ttf/cmr10.ttf')
plt.rcParams['font.serif']=cmfont.get_name()
plt.rcParams['mathtext.fontset']='cm'
plt.rcParams['axes.unicode_minus']=False

path = "/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/twoSideDeriv/derivOutput/"

# redshifts = ["06.03", "07.57", "09.04", "11.99", "15.15", "17.92"] #whole range 
# redshifts = ["06.46", "08.09", "09.45", "11.99", "14.52"] #even smaller redshifts
redshifts = ["06.17", "08.65", "11.00", "13.34"] #even smaller redshifts
# redshifts = ["06.03", "07.08", "08.09", "09.04"] #even smaller redshifts
# redshifts = ["11.00", "13.06", "16.14", "19.08"] #higher redshifts 11 13 16 19

params = ["zeta", "tvir", "fstar", "zetaX", "mFDM"]#rmax no longer used
numWavenumbers = 13
numZs = len(redshifts)
numParams = len(params)

fig, axes = plt.subplots(numParams, numZs, sharex=True, sharey=True, figsize=(15, 15))
# fig, axes = plt.subplots(numParams, numZs, sharex=True, sharey=True, figsize=(19, 15))
# fig, axes = plt.subplots(numParams, numZs, sharex=True, sharey=True, figsize=(24, 21))
plt.xscale('log')
plt.yscale('symlog')

paramToLatexDict = dict(
	{
		"zeta": r"{\zeta}", 
		"tvir": r"{T_{\rm vir}}",
		"fstar": r"{f_\star}",
		"zetaX": r"{\zeta_X}",
		"mFDM": r"{m_{\rm FDM}}"
	})

def graphboi(x, y, z, p, redshift, param):
	# plt.yticks(fontsize=10)
	axes[p, z].plot(x, y)
	#short circuiting causes conditional evaluation only when LHS of the AND is true
	p == 0 and axes[p, z].set_title(r"$z=$"+str(float(redshift)))
	axes[p, z].set_xlabel(r"k (Mpc$^{-1}$)") 
	axes[p, z].set_ylabel(
		(r"$\frac{{\partial \Delta^2_{{21}}}}{{\partial q_{}}}$ (mK$^2$)".format(paramToLatexDict[param])), 
		fontsize=24)
	axes[p, z].tick_params(axis='y', labelsize=12)
	return

for z in range(numZs):
	currZ = redshifts[z]

	for p in range(numParams):
		currP = params[p]

		#find the right file
		#files are named fisher_derivative_<param>_z0<XX.XX>.txt
		filepath = glob(path + "*_" + currP + "_z0" + currZ + "*")[0]
		# print(filepath)
		data = open(filepath, 'r')

		#get data from file
		k = []
		dPS = []
		for _ in range(numWavenumbers):
			lineOfData = data.readline()
			k.append(float(lineOfData.split()[0]))
			dPS.append(float(lineOfData.split()[1]))

		#Graph the data
		graphboi(k, dPS, z, p, currZ, currP)
# plt.tight_layout()
for x in axes.flat:
	x.label_outer()
# plt.show()

plt.savefig("/Users/richardchen/Desktop/summerResearch/2020summer/fiducialFisherMatrix/twoSideDeriv/powSpecDeriv2.pdf") #save

#redshifts = ["13.06", "14.22", "14.52", "14.83", "15.15", "17.92"] #weird transition
#redshifts = ["06.03", "07.08", "08.09", "09.04", "10.09", "11.00"] #smaller redshifts
#subplots - double nested for loop, for (z): for (param) to get subplot position, 
#function that takes in z, param and graphs dpower spectrum
# p == numParams - 1 and axes[p, z].set_xlabel("z="+str(float(redshift))) #along bottom
# z == 0 and axes[p, z].set_ylabel(param) #along left side
#Logic unnecessary; replaced by label_outer()

