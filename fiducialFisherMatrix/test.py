import matplotlib.pyplot as plt
from glob import glob
import sys

import matplotlib.font_manager as font_manager
import matplotlib as mpl

plt.rcParams.update({"text.usetex": True})#, "font.size": 24})

plt.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + '/fonts/ttf/cmr10.ttf')
plt.rcParams['font.serif']=cmfont.get_name()
plt.rcParams['mathtext.fontset']='cm'
plt.rcParams['axes.unicode_minus']=False

print("$\\frac{\partial \Delta^2_{21}}{\partial q_{}}$ (mK$^2$)")
       $ \frac{\partial \Delta^2_{21}}{\partial q_{}}$ (mK$^2$)
