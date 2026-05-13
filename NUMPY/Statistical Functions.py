import numpy as np

a=np.array([1,-1,1,-1])
#Get the mean of the numpy array
mean=a.mean()
print("Mean value:",mean)
#get the standared deviation of numpy array
s_d=a.std()
print("Standared deviation:",s_d)

b=np.array([-1,2,3,4,5])
#get the biggest value of array
print("Max:",b.max())
#get the smallest value in the numpy array
print("Min:",b.min())