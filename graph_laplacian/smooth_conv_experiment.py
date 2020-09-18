import numpy as np
from scipy.signal import convolve2d

f1 = np.array([[1,-1],[1,-1]]) # sin(x)
f2 = np.array([[1,1],[-1,-1]]) # sin(y)

print(convolve2d(f1,f2,mode='same',boundary='wrap'))
