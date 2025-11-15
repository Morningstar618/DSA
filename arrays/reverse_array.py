"""
Reverse an array
"""

def reverse_array(arr: list) -> list:
    length = int(len(arr) / 2)

    for i in range(length):
        last_index = len(arr) - 1 - i
        temp = arr[i]
        arr[i] = arr[last_index]
        arr[last_index] = temp

    return arr


if __name__ == '__main__':
    nums = [1, 2, 3 , 4]
    print(reverse_array(nums))

    nums1 = [1, 2, 3, 4, 5]
    print(reverse_array(nums1))
