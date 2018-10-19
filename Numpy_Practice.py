import numpy as np

#Printing a simple 3*3 Array
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("The array is")
print(a)

#Printing the Array dimension
print("The dimensions are")
print(a.ndim)

#Printing itemsize
print("The itemsize is ")
print(a.itemsize)

#Printing the type stored in Numpy Array
print("The data-type stored in array is ")
print(a.dtype)

#Printing the size of Array OR Total number of elements in y
print("Total number of elements in Array:-")
print(a.size)

#Printing the shape of Numpy Array
print("Shape of array is:-")
print(a.shape)

#Re-shaping an Array
b = np.array([(1,2,3,4),(5,6,7,8)])
print("Before reshaping, array was:-")
print(b)
Brshp = b.reshape(4,2)
print("After reshapping, array is ")
print(Brshp)

#Accessing a particular element

print("The element at 2,2 is "+ str(a[2,2]))
print("The element at 1,0 is "+str(a[1,0]))


#Slicing a numpy array

A = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print("The sliced array is:-")
print(A[0:2,2])


#Getting Equally spaced values between two numbers:-

V1to10by5 = np.linspace(1,10,5)
print("1 to 10 equally spaced:-")
print(V1to10by5)

#Getting Max, Min and sum

a = np.array([(1,2,3),(4,5,6),(7,89,0)])
print("Max of array: "+ str(a.max()))
print("Min of array: "+ str(a.min()))
print("Sum of all elements in array: "+ str(a.sum()))

#Axis Sums (Sums on Rows and sums on Columns)

a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("Column vise sum is "+ str(a.sum(axis=0))) #Column vise sum
print("Row vise sum is "+ str(a.sum(axis=1))) #Row vise sum

#Finding the Square root and Stdev
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("The square rooted array is :-")
print(np.sqrt(a)) #getting Square roots
print("Stdev in Array elements is "+ str(np.std(a)))

#Basic Mathematical Operations
A = np.array([(1,2,3),(4,5,6)])
B = np.array([(10,20,30),(40,50,60)])

print("Sum:-")
print(A+B)

print("Difference:- ")
print(A-B)

print("Element vise Product:-")
print(A*B)

print("Element vise Division:-")
print(A/B)


#Vertical Stacking

print("AFter vertical stacking:-")
print(np.vstack((A,B)))

#Horizontal Stacking

print("AFter horizontal stacking:-")
print(np.hstack((A,B)))


#Merging all elements row vise into a single dimensional list
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("Merging via Ravel function:-")
print(a.ravel())


















