import numpy as np
# Create a list

a=[[11,12,13],[21,22,23],[31,32,33]]
A=np.array(a)
print(A)
# we can use all the methods that we use for vector or 1D array 
#like .ndim,.shape,.size etc
#Accessing different elements of Numpy Array
print(A[2,2])
print(A[2][2])
print(A[0][0:2])
print(A[0:2,2])

#Basic operations
b=[[1,2,3],[4,5,6],[7,8,9]]
B=np.array(b)
print(A+B)
print("Multiplication:\n")
print(np.multiply(A,B)) #or use A*B
print("Dot operation:\n")
print(np.dot(A,B))

print("Transpose:\n")
print(A.T)