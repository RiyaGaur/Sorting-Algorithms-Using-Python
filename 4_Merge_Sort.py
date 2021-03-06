def Merge_Sort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]
  
        Merge_Sort(L)
        Merge_Sort(R) 
  
        i, j, k = 0, 0, 0       
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
           
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1



array = [6, 5, 12, 10, 9, 1]
Merge_Sort(array)
print("Sorted array is: ")
print(array)
