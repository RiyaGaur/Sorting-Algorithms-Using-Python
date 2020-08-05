def Partition(array, low, high):

    p = array[high]
    i = low - 1
    print(p, " is the pivot.")
    for j in range(low, high):
        if array[j] <= p:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
        

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print(array)
    return i + 1 


def QuickSort(array, low, high):
    if low < high:
        pi = Partition(array, low, high)
        QuickSort(array, low, pi - 1)
        QuickSort(array, pi + 1, high)


data = [2,5,1,7,9,12,11,10]
size = len(data)
QuickSort(data, 0, size - 1)
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print('Sorted Array in Ascending Order:')
print(data)

