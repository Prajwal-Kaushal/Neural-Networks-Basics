'''
Rather than typing in the random input data. We will use a function that can create 
non-linear data.

First do - 

pip install nnfs

'''


import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

import matplotlib.pyplot as plt

X, y = spiral_data(samples=100, classes=3)

plt.scatter(X[:,0], X[:,1])
plt.show()
#%%
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()