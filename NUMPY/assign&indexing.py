# we can assign and get the values by put list into the argument like a[1]
# where instead of 1 we put an actual list like select=[1,2,3,4]
# and get the output as a[select],as a return we will get all values of corroseponding index
# We also assign value like this a[0,1,3,4]=12,3,43,54
# or like this a[0:4]=23,12,42,14 
import numpy as np

a=np.array([34,53,25,23])
select=[1,3]
print(a[select])
again=[0,2]
a[again]=100,200
print(a)
a[0:3]=100,200,300
print(a)

#some other methods like 
#a.size== tell us about the size of numpy array
#a.ndim -->tell use about the dimention of numpy array
#a.shape -->tell use the shape/size of the numpy array
