import numpy as np
a=np.array([0,1,2,3,4])#create a numpy array
#print(a)
#print each element
print("a[0]:",a[0])
print("a[1]:",a[1])
# checking numpy version
print(np.__version__)
# if we check the type of the array we get numpy.ndarray:
print(type(a))
# for data type we use a.dtype
print(a.dtype)

b=np.array([3.1,11.02,6.2,213.2,5.2])
#slicing
c=b[1:4]
print(c)
