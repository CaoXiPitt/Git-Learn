# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:31:07 2018

@author: HatLabUnderGrad2
"""

# test of the interpolation
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num = 11, endpoint = True)
#z = np.linspace(10, 20, 11)
#y = np.exp(-x)#np.cos(-x**2/9.0)
y = 0.1*np.cos(-x**2/9.0) + np.random.rand(11)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num = 41, endpoint = True)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()