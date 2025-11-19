"""
Find the maximum difference between two elements in the array
while maintaing the order.

i/p: [2, 3, 10, 6, 4, 8, 1]
o/p: 8 i.e. 10 (index 2) - 2 (index 0)
"""

def max_diff(nums: list) -> int:
    res = nums[1] - nums[0]
    min_val = nums[0]

    for i in range(1, len(nums)):
        res = max(res, nums[i] - min_val)
        min_val = min(min_val, nums[i])

    return res


if __name__ == '__main__':
    nums1 = [2, 3, 10, 6, 4, 8, 1]
    print(max_diff(nums1))
