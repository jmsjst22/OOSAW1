import numpy as np
filename='data.txt'
x,y=np.loadtxt(filename, unpack=True, dtype=float, comments='#',usecols=(0,1))

print(min(x))
