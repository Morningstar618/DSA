"""
========== Selection sort ==========

Time -> O(n^2)

This sorting algorithm does less memory writes
when compared to QuickSort, MergeSort, Insertion sort,
etc. But Cycle sort is optimal in terms of memory writes.
Memory writes is a critical operation when it comes to
EEP ROMs and alike. If we do more writes in an EEP ROM,
its available memory reduces.

HeapSort is inspired by this algorithm.

It is not a stable algorithm. (order of equal elements
may change).

Sorts the array in-place. Does not require extra 
memory to do the same.

Basic Idea: We find out the minimum element and then
put it at the 1st position, then we find the 2nd element
and put it at the 2nd position and so on. 
"""

def selection_sort(arr: list):
    "Selection sort implementation"
    n = len(arr)

    for i in range(n - 1):
        min_val = arr[i]

        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                min_val = arr[j]

            if min_val != arr[i]:
                temp = arr[i]
                arr[i] = min_val
                arr[j] = temp


if __name__ == '__main__':
    x = [12, 3, 5, 7, 1, 9]
    selection_sort(x)

    print(x)
