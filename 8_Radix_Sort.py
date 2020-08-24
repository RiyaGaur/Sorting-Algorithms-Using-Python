def RadixSort(nums):
    r = 10
    place = 1
    maximum = max(nums)

    while place < maximum:
      buckets = [list() for _ in range( r )]
      for i in nums:
        tmp = int((i / place) % r)
        buckets[tmp].append(i)
      a = 0
      for b in range( r ):
        bucket = buckets[b]
        for i in bucket:
          nums[a] = i
          a += 1
      place *= r
      print(nums)
    return nums

data = [10,50,4,2,1,100,200]
sorted = RadixSort(data)
print('Sorted Array:',sorted)
