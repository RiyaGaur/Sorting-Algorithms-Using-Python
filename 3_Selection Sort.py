def selectionSort(array):
   
    for i in range(len(array)):
        min = i

        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j

        temp=array[i]
        array[i]=array[min]
        array[min]=temp


data = [20,50,10,70,80]
selectionSort(data)
print('Sorted Array:',data)
