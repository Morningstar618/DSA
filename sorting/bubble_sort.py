"""
Bubble sort implementation in Python
"""

def bubble_sort(arr):
    """Bubble sort"""
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if swapped is False:
            break


if __name__ == '__main__':
    nums1 = [10, 8, 20, 5]
    bubble_sort(nums1)
    print(nums1)
