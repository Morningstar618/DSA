"""
Lomuto partition implementation in Quick sort.

Here, we will assume the last element of the array
as the pivot element. It works well when the pivot 
is always the last element.

In case you pant to partition the array on a specific
index, just swap it with the last element of the array.

Time -> O(n), Space -> O(1)
"""

def lomuto(arr: list, high: int, low: int=0) -> int:
    """Lomuto partition"""

    # Helper ---------------------------------------
    def swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    # Lomuto ---------------------------------------
    pos = -1

    for i in range(low, high):
        if arr[i] < arr[high - 1]:
            pos += 1
            swap(arr, i, pos)

    pos += 1
    swap(arr, pos, high - 1)

    return pos


# Main ----------------------------------------------
if __name__ == '__main__':
    # Pivot element in normal range
    nums = [10, 80, 30, 90, 40, 50, 70]
    print(nums, 'pivot:', lomuto(nums, len(nums)))

    # Pivot element lowest
    nums = [10, 80, 30, 90, 40, 50, 5]
    print(nums, 'pivot:', lomuto(nums, len(nums)))

    # Pivot element highest
    nums = [10, 80, 30, 90, 40, 50, 97]
    print(nums, 'pivot:', lomuto(nums, len(nums)))
