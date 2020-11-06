# Sorting-Algorithms-Using-Python

## 1. Insertion Sort
#### stable: Yes 
#### time: O(n^2)
#### space: O(1) 

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

## 2. Bubble Sort
#### stable: Yes 
#### time: O(n^2)
#### space: O(1) 

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

## 3. Selection Sort
#### stable: No
#### time: O(n^2)
#### space: O(1) 

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
<br>
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.


## 4. Merge Sort
#### stable: Yes
#### time: O(nlogn)
#### space: O(n)

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
