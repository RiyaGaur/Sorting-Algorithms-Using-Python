def Insertion_Sort(array):
    for i in range(1,len(array)):
        temp=array[i]
        temp2=i-1
        while temp2>=0 and array[temp2]>temp:
            array[temp2+1]=array[temp2]
            temp2=temp2-1
        array[temp2+1]=temp
    return array

n= int(input("Enter no of test cases:"))
for i in range(0,n):
    arr=[]
    size=input("Enter the size:")
    print ('Enter numbers in array: ')
    for i in range(int(size)):
        n = input("number :")
        arr.append(int(n))
    print ('Array: ',arr)
    print("Sorted Array: ",Insertion_Sort(arr))

