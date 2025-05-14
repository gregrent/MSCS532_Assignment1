#########################################
# MSCS 532 Assignment 1
# Author: Gregory Renteria
# Insertion sort algorithm that sorts
# in monotonically decreasing order.
#########################################

#  A (list): The list of elements to be sorted.
#  n (int): The number of elements in the list A.
def insertionSort(A, n):
   print ("insertionSort called") # placeholder for now
   for i in range(0, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
   print(A)


# Temporary test call
A = [73, 8, 42, 19, 91, 27, 5, 64, 33, 50]
insertionSort(A, len(A))