"""
Left rotate an array by 1

i/p: [30, 5, 20]
o/p: [5, 20, 30]
"""

def rotate(nums: list):
    nums_len = len(nums)
    temp = nums[0]

    for i in range(nums_len - 1):
        nums[i] = nums[i + 1]

    nums[nums_len - 1] = temp


if __name__ == '__main__':
    nums1 = [30, 5, 20]
    rotate(nums1)
    print(nums1)
