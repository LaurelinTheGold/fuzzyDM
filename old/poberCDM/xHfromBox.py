from glob import glob
import numpy as np
import struct as s

z_xH = []
ave_xH = []
path2 = "/Users/richardchen/Desktop/summerResearch/2020summer/poberCDM/"

d = open("".join(glob(path2 + "xH_*")), 'r')
def make_array(data):
    d = 256
    array = np.zeros((d,d,d))
    for i in range(d):
        for j in range(d):
            for k in range(d):
                b = data.read(4)
                l = s.unpack('f', b)[0]
                array[i][j][k] = l
    new_array = np.reshape(array, d ** 3)
    return(new_array)

a = make_array(d)
print(np.mean(a))

