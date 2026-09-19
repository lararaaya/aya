def binary_search (arr, x):
    left = 0
    right = len(arr) -1

    while left <= right:
       mid = (left + right) // 2
       if arr[mid] == x:
         return True
       elif arr[mid]  < x:
         left = mid + 1
       else:
         right = mid -1
    return False 
print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8,], 5))

def power(a, b):
  result = 1
  for i in range(b):
    result = result * a
  return result
print(power(3, 4))

def bubbleSort(nlist):
  for passnum in range(len(nlist)-1, 0, -1):
    for i in range(passnum):
      if nlist[i] > nlist[i+1]:
        temp = nlist[i]
        nlist[i] = nlist[i+1]
        nlist[i+1] = temp
  return nlist   
nlist = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(bubbleSort(nlist))  

def mergeSort(mylist):
  if len(mylist) > 1:
    mid = len(mylist) // 2
    left = mylist[:mid]  
    right = mylist[mid:]
    mergeSort(left)
    mergeSort(right)
    i = 0
    j = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        mylist[i+j] = left[i]
        i = i + 1
      else:
        mylist[i+j] = right[j]
        j = j + 1
    while i < len(left):
        mylist[i+j] = left[i]    
        i = j + 1
    while j < len(right):
        j = j + 1
  return mylist 
myList = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(mergeSort(myList))  

def quickSort(array, start, end):
  if start >= end:
    return
  pivot = array[start] 
  low = start + 1
  high = end
  while True:
    while low <= high and array[high] >= pivot:
      high = high - 1
    while low >= high and array[high] >=pivot:
      low = low + 1
    if low >= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  array[start], array[high] = array[high], array[start]
  return high

"""
quickSort(array, start, high -1)
  quickSort(array, high + 1, end)
"""
array = [29, 13, 22, 37, 52, 49, 46, 71, 56]
quickSort(array, 0, len(array) - 1)
print(array)  

                        
  
         
