"""
Binary search: recursive

i/p: [1, 2, 3, 4, 5, 6], k = 4
o/p: 3

i/p: [1, 2, 3, 4], k = 8
o/p: -1

NOTE: Iterative implementation is better.
    1. No recursive function call overhead.
    2. Requires only O(1) space compared to
       O(logn) for the recursive implemention.
"""

def b_search(nums, s, e, k) -> int:
    """
    recursive implementation for binary
    search
    """
    m = int((s + e) / 2)

    if nums[m] == k:
        return m

    if nums[m] > k:
        e = m - 1
    else:
        s = m + 1

    if s > e:
        return -1

    return b_search(nums, s, e, k)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    print(b_search(nums1, 0, len(nums1) - 1, k=4))  # 3

    nums2 = [1, 2, 3, 4]
    print(b_search(nums2, 0, len(nums2) - 1, k=8))  # -1
