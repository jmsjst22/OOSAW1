#bubble
import numpy as np
#create "array" which is a numpy array of random numbers
array=np.random.random((20))

def bubble(array):
  n = len(array)

  for i in range(n):
    already_sorted = True

    for j in range(n-i-1):
#if value is bigger than next value
      if array[j] > array[j+1]:
#swap them
        array[j], array[j+1] = array[j+1], array[j]
#note, this function is inefficient and may have take a lot of clock time with both well ordered and badly sorted arrays

        already_sorted = False

    if already_sorted:
      break

  return array

bubble(array)
print(array)
