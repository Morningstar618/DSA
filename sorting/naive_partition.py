"""
Naive partition quick sort implementation.

Time -> O(n), Space -> O(n)
"""

def naive(arr: list, low: int, high: int, pivot_index: int):
    """Naive partition quick sort implementation."""
    # Create a temporary array just for the current slice
    temp = [0] * (high - low)
    index = 0
    pivot_val = arr[pivot_index]

    # 1. Copy elements smaller than or equal to pivot
    for i in range(low, high):
        if i == pivot_index:
            continue  # Skip the pivot itself for now
        if arr[i] <= pivot_val:
            temp[index] = arr[i]
            index += 1

    # 2. Copy the pivot element (It belongs between the two sections)
    # This stores the position where the pivot lands, useful for recursion later
    pivot_pos = index
    temp[index] = pivot_val
    index += 1

    # 3. Copy elements higher than pivot
    for i in range(low, high):
        if i == pivot_index:
            continue
        if arr[i] > pivot_val:
            temp[index] = arr[i]
            index += 1

    # 4. Copy elements from temp back to the original array
    # pylint: disable=consider-using-enumerate
    for i in range(len(temp)):
        arr[low + i] = temp[i]

    # Return the new index of the pivot (essential for QuickSort recursion)
    return low + pivot_pos


if __name__ == '__main__':
    nums = [5, 13, 6, 9, 12, 11, 8]

    # Partitioning around index 6 (value 8)
    # Expected result: [5, 6, 8, 13, 9, 12, 11] (Order of larger elements stays stable)
    # pylint: disable=invalid-name
    p_index = naive(nums, 0, len(nums), len(nums) - 1)

    print(f"Partitioned Array: {nums}")
    print(f"Pivot is now at index: {p_index}")
