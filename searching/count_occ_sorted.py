"""
Find the no. of occurrences of a given element
in a sorted array.

i/p: [10, 20, 20, 20, 40, 40], k=20
o/p: 3

Approach: last occurrence - first occurence + 1
Time -> O(logn), Space -> O(1)
"""

def first(nums: list, k: int) -> int:
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


def last(nums: list, k: int) -> int:
    """Find last occurrence of 'k'
    in 'nums'"""
    s = 0
    e = len(nums) - 1
    m = int((s + e) / 2)

    while s <= e:
        if nums[m] == k and m == len(nums) - 1 or nums[m] == k and nums[m + 1] != k:
            return m

        if nums[m] > k:
            e = m - 1
        else:
            s = m + 1

        m = int((s + e) / 2)

    return -1


def count_occ(nums: list, k: int) -> int:
    """Find frequency of 'k' in array 'nums'."""
    first_occ = first(nums, k)
    if first_occ == -1:
        return 0

    return last(nums, k) - first_occ + 1


if __name__ == '__main__':
    print(count_occ([10, 20, 20, 20, 40, 40], 20))  # 3
    print(count_occ([10, 10], 10))                  # 4
    print(count_occ([1, 2, 3], 4))                  # 0
