def heapify(arr, n, i):
      lrgst = i
      l = 2 * i + 1
      r = 2 * i + 2
      if l < n and arr[i] < arr[l]:
          lrgst = l
      if r < n and arr[lrgst] < arr[r]:
          lrgst = r
      if lrgst != i:
          arr[i], arr[lrgst] = arr[lrgst], arr[i]
          
          heapify(arr, n, lrgst)
  
def heapSort(arr):
      n = len(arr)
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)
      return arr
  
  
arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is",heapSort(arr))

  
