"""
Left rotate array by `n` places.

i/p: [1, 2, 3, 4, 5], n = 3
o/p: [4, 5, 1, 2, 3]
"""

# Theta(n) time and space complexity
def rotate(nums: list, n: int) -> list:
    rotated = []
    length = len(nums)

    for i in range(length):
        x = (i + n) % length
        rotated.append(nums[x])

    return rotated


# Best approach - Reverse Algo -----------------------
# Theta(n) time and Theta(1) space
def left_rotate(nums: list, n: int):
    length = len(nums)

    reverse(nums, 0, n - 1)
    reverse(nums, n, length - 1)
    reverse(nums, 0, length - 1)


def reverse(nums: list, low: int, high: int):
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low += 1
        high -= 1



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = left_rotate(nums, 3)
    print(nums)
