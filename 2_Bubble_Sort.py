def Bubble_Sort(array):
    for j in range(0,len(array)-1):
        for i in range(0,len(array)-1):
            if array[i]>array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
    return array

arr=[5,1,4,2,8]
print(Bubble_Sort(arr))
