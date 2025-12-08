"""
Find the first occurrence of `k` in a sorted array.
If the element is not found, return -1.

Approach: Binary search

Time -> O(logn), Space -> O(1)

i/p: [1, 10, 10, 10, 20, 20, 40], k=20
o/p: 4
"""

def find(nums: list, k: int) -> int:
    """Find 1st occurrence of 'k'
    in 'nums'"""
    s = 0
    e = len(nums) - 1
    m = int((s + e) / 2)

    while s <= e:
        if nums[m] == k and nums[m - 1] != k or m == 0:
            return m

        if nums[m] >= k:
            e = m
        else:
            s = m + 1

        m = int((s + e) / 2)

    return -1


if __name__ == '__main__':
    nums1 = [1, 10, 10, 10, 20, 20, 40]

    print(find(nums1, 20))      # 4
    print(find(nums1, 50))      # -1
    print(find([1, 1, 1], 1))   # 0
