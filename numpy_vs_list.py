import numpy as np
import sys
import time


#Space Comparison
s = range(1000)
Size = sys.getsizeof(s[5])*len(s)
print("Space occupied by list:- "+str(Size))

a = np.arange(1000)
Size = a.size * a.itemsize
print("Space occupied by numpy array:- "+str(Size))

#Time Comparison
L1 = range(1000)
L2 = range(1000)

NPA1 = np.arange(1000)
NPA2 = np.arange(1000)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
TIME_TAKEN = (time.time()-start)*1000
print("Time taken for adding two lists:- " + str(TIME_TAKEN) + " ms")

start = time.time()
result = NPA1+NPA2
TIME_TAKEN = (time.time()-start)*1000
print("Time taken for adding two lists:- " + str(TIME_TAKEN) + " ms")

