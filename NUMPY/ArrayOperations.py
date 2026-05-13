import numpy as np

# array addition
u=np.array([1,0])
v=np.array([0,1])

print(u+v)# or we can use z=np.add(u,v)
#substraction
print(u-v)# or we can use z=np,substract(u,v)
#array Multiplication

x=np.array([1,2,4])
y=np.array([2,1,5])

z=np.multiply(x,y)
print(z)
print(x*y)

#Array division:
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([2,1,2,3,4,5])
arr3=np.divide(arr1,arr2)
print(arr3)
print(arr1/arr2)

#dot product the actual array multiplication what we do in math row into column
X=np.array([1,2])
Y=np.array([3,2])
#calculate the dot product
Z=np.dot(X,Y)
print("Dot product of X,Y:",Z)

#adding constant to the numpy array 
print(Z+1)
#Mathematical Functions like pi, sin,cos etc
#Create the numpy array in radians

p=np.array([0,np.pi/2,np.pi])
q=np.sin(p)
print(q)