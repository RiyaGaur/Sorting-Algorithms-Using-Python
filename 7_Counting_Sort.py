def CountingSort(arr):
    n = len(arr)
    m = max(arr)
    count = []
    for i in range(0,100):
        count.append(0)
    for i in arr:
        count[i] += 1
    output = []
    for i in range(0,len(count)):
        if count[i] > 0:
            for j in range(0,count[i]):
                output.append(i)
    return output

data = [3,4,4,5,3,6,2,2,1,4,1,7,9,12]
print("Sorted arr in Ascending Order: ",end="")
print(CountingSort(data))

    

