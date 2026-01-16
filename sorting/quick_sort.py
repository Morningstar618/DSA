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

def lomuto(arr: list, low: int, high: int) -> int:
    """Lomuto partition"""

    # Helper ---------------------------------------
    def swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    # Lomuto ---------------------------------------
    pos = low - 1

    for i in range(low, high):
        if arr[i] < arr[high]:
            pos += 1
            swap(arr, i, pos)

    pos += 1
    swap(arr, pos, high)

    return pos


def hoare(arr: list, low: int, high: int):
    "Hoare partition implementation"
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right; stops when it finds an element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left; stops when it finds an element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, return the split point
        if i >= j:
            return j

        # Swap the elements to put them on the correct sides
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list, low: int, high: int):
    "Quick sort using Lomuto"
    if low < high:
        p = hoare(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


if __name__ == '__main__':
    nums = [8, 4, 7, 9, 3, 10, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
