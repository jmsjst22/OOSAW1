#selection sorting
import numpy as np
#create "array" which is a numpy array of random numbers
array1=np.random.random((20))

def selecto(array1):
#using built in range function to apply to variable to convert into acceptable dtype
  indexlength = range (0, len(array1)-1)
#accepting minimum value as the first the algorithm processes
  for i in indexlength:
      min_value = i
#nested counter argument
      for j in range(i+1, len(array1)):
#contesting that if identical value stream 2 (which is one int ahead) is lower than min_value
        if array1[j] < array1[min_value]:
#then j is assigned to new min_value
          min_value = j
#if min_value is j then the two values are switched in the array
      if min_value != i:
          array1[min_value], array1[i] = array1[i], array1[min_value]
#return array1 product outside of loop.
  return array1

print(selecto(array1))
