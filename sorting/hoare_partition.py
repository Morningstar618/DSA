"""
Hoare partition implementation in Quick sort.

This partition algorithm works better than Lomuto
partition wrt efficiency. But Lomuto ensures that
the pivot is at the correct place which Hoare doesn't. 

Time -> O(n), Space -> O(1)

Unlike Lomuto, the first element here is considered
the pivot.

It is an unstable partition algorithm. And it is one of
the reason that the Quick Sort algorithm is not a stable
sorting algorithm by default.
"""

def hoare(arr: list, low: int, high: int):
    """Hoare partition"""

    # Helpers ---------------------------
    def swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    # Hoare -----------------------------
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Traverse from the left till we find an element smaller than
        # pivot
        while True:
            i += 1
            if arr[i] > pivot or i == 0:
                break

        # Traverse from the right till we find an element greater than
        # pivot
        while True:
            j -= 1
            if arr[j] < pivot:
                break

        if i >= j:
            return j

        swap(arr, i, j)


if __name__ == '__main__':
    # Linters --------------------
    # pylint: disable=invalid-name

    nums = [5, 3, 8, 4, 2, 7, 1, 10]
    res = hoare(nums, 0, len(nums) - 1)
    print(nums, 'partition:', res)
