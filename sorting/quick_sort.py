"""
-------- Quick Sort Introduction ---------

1. Divide and Conquer Algorithm
2. Worst case Time complexity -> O(n^2)
3. Despite O(n^2) worst case, it is considered
   faster, because of the following reasons.
   a. In-place
   b. Cache friendly
   c. Average case is O(nlogn)
   d. Tail recursive
4. Partition is the key function (Naive, Lomuto, Hoare)
   Quick sort is stable when we use Naive partition algorithm.
5. If we don't need stability, quick sort is actually the
   fastest algorithm which is used in libraries also. But
   if stability is required, then merge sort is preferred.
"""