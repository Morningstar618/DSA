# Overview of Sorting Algorithm
Special cases and the correct Algorithm to use in every case.

## Special Cases

### 1. Binary Array
These are arrays where only two values are available. For example **[0, 1, 1, 0, 1, 0]**. The best algorithm to use in this case would be the `Partition Algorithm of Quick Sort`.

Partition algorithms of Quick sort are as follows:
- Lomuto partition scheme
- Hoare partition scheme
- Naive partition scheme

Naive is stable while while Lomuto and Hoare are quicker as Naive requires extra space. Also, Hoare is faster than Lomuto.

### 2. Array with three values
This is a special case where we have three unique values in the array. Once again, for these kind of cases, we can use any one of the `Partition algorithms of Quick Sort`.

### 3. Array of size `n` and small ranged values
An example of this case would be an array of size `n` (1000) and `k` (100 to 200) unqiue values. Here we can use the `Counting Sort` algorithm.

- Time Complexity:    O(n + k)
- Space Complexity:   O(k)

### 4. Array of size `n` and range is of size `n^2` or `n^3` or closer
Optimal algorithm for this scenario would be the `Radix sort`.

- Time complexity:  O(n)
- Space complexity: O(n)

### 5. Array of uniformly distributed data over a range
`Bucket sort` can be used when our data is uniformly distributed. It is this fastest of all sorting algorithms for this particular case. It can sort in **linear time**.

### 6. When memory writes are costly
Memory writes are costly when every write reduces the age of our memory. For example **EEPROM**. We have two algorithms for this case.

- **Selection sort** -> simple algo that does minimum swaps compared to other algos. Its worst case time complexity is `O(n^2)`.

- **Cycle sort** -> optimal for memory writes and better than selection sort. Its worst case time complexity is also `O(n^2)`.

### 7. When adjacent swaps are allowed
In a case where we are allowed only to swap adjacent elements, then we can use `bubble sort`. There is an optimised version of bubble sort i.e. `cocktail sort`. Bubble sort traverses from left to right while cocktail sort traverses from both the sides.

### 8. When array size is small
For such cases we have two general purpose algos. `Selection sort` and `Insertion sort`. Among these two **insertion sort** works best. It is considered the best algorithm when we want to sort small number of elements. In many stdlib sorting algos, they switch to insertion sort when the array size to sort is small (10-20).

### 9. When available extra memory is small
Here, `shell sort` would be the optimal algorithm as it **does not use any extra space** and sorts the array **in-place**. We have other algos as well that do not use extra space like selection sort and insertion sort but shell sort is better in terms of time complexity (`O(n * (logn) ^ 2`).


## General Purpose algorithms
It has been mathematically proven that we cannot sort an array whose data and size are not known to us in less than **O(nlogn)** time. So we need atleast that much time to sort an unknown random array. And we have some algos for such cases.

- **Merge sort** -> Time **O(nlogn)**. Stable algo. Good for linked lists. Good when we have data on a tape drive or we need to access it sequentially. It is also well suited for external sorting. 

- **Heap sort** -> Time **O(nlogn)**. 

- **Quick sort** -> Time complexity is **O(n^2)** in worst case but `works better than Merge and Heap sort on average`.

In general when we compare these three algos, `quick sort` is the fastest of them all. But merge sort is better for some cases, like its a **stable sorting algo**. Both of these algos are `divide and conquer`, so they parallelize really well. We can reduce the time complexity further by parallelizing these algorithms.


## Hybrid Sorting algorithms (used in libraries)
Most of the library functions, they use a hybrid sorting algorithm, a sorting algorithm, which is a mix of two or three basic sorting algorithms.

- **Tim sort** -> used in python, its a `mix of insertion sort and merge sort`. It uses merge sort for general purpose data and when the array size is small or becomes small during recursive calls, it switches to insertion sort.

- **Intro sort** -> it's a mix of quick sort, heap sort and insertion sort. In general it uses quick sort, and when your quick sort is doing many unfair partitioning and the number of recursion calls are going beyond logn, it switches to heap sort. And when the array size becomes small, it switches to insertion sort.


## Stability
Stability in sorting means to preserve the order of the items in the original array after sorting. Its important only when we have an
object associated with the sorted value.

Consider this example -> **[("Anil", 50), ("Ayan", 80), ("Piyush", 50), ("Ramesh", 80)]**
After sorting this will be -> **[("Anil", 50), ("Piyush", 50), ("Ayan", 80), ("Ramesh", 80)]**

Note that the order was maintained, i.e. Anil's order and the others order was maintained during the sort as it was in the original
array.

Stability is not important when we are sorting an array of integer values or other scalar values.

An unstable order won't care of the order -> **[("Piyush", 50), ("Anil", 50), ("Ayan", 80), ("Ramesh", 80)]**

### Stable sorting algorithms
- Bubble sort
- Insertion sort
- Merge sort

### Unstable sorting algorithms
- Selection sort
- Quick sort
- Heap sort