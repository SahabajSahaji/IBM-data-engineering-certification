#A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.

# numpy.linspace(start, stop, num = int value)

# start : start of interval range

# stop : end of interval range

# num : Number of samples to generate.

import numpy as np
import  matplotlib.pyplot as plt

#Makeup a numpy array within [-2,2] and 5 elements
a=np.linspace(-2,2,num=5)
print(a)
#b=np.linspace(0,1,50)
#print(b)
print(np.linspace(5,4,6))

#make a array within [-2,2]and 5 elements
x=np.linspace(0,2*np.pi,num=100)
y=np.sin(x)

plt.plot(x,y)
plt.show()