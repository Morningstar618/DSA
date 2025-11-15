"""
Check if the array is sorted
"""

def is_sorted(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


if __name__ == '__main__':
    res = is_sorted([1, 3, 6, 6, 8, 11])
    print(res) # true

    res = is_sorted([1, 3, 16, 8, 11])
    print(res) # false

    res = is_sorted([11])
    print(res)
