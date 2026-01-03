"""
============== Merge Sort ==============

1. It is a divide and conquer algorithm.
2. Stable Algorithm.
3. O(nlogn) Time and O(n) Aux Space.
4. Well suited for Linked lists. Works in 
   O(1) Aux space. Best time complexity we
   can get in a single processor with random
   input.
5. Used in external sorting.
6. In general for arrays, quick sort outperforms
   it. (Not true for linked lists).
"""

def merge_sort(arr):
    """
    Efficient merge sort implementation with O(n log n) time complexity.
    
    Args:
        arr: List of comparable elements to sort
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: Sorted list
        right: Sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0

    # Compare elements from left and right, append smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 1, 2, 1]
    ]

    for arr in test_arrays:
        print(f"Original: {arr}")
        print(f"Sorted:   {merge_sort(arr)}")
        print()
