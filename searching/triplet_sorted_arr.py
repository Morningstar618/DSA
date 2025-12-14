"""
Find triplet in a sorted array such that
the sum of triplet is equal to 'k'.

i/p: [2, 3, 4, 8, 9, 20, 40], k = 32
o/p: True

Approach: Find a pair that is equal to 'k'
when 'arr[i]' is subtracted from it.

`k - arr[i] = pair[i+1:]`

Time -> O(n^2), Space -> O(1)
"""

def is_pair(nums: list, k: int) -> bool:
    """Find pair in 'nums' with sum 'k'."""
    s = 0
    e = len(nums) - 1

    while s < e:
        x = nums[s] + nums[e]

        if x == k:
            return True

        if x > k:
            e -= 1
        else:
            s += 1

    return False


def triplet(nums: list, k: int) -> bool:
    """Find triplet in 'nums' with sum
    equal to 'k'."""

    for i, num in enumerate(nums):
        if is_pair(nums[i+1:], k - num):
            return True

    return False


if __name__ == '__main__':
    nums1 = [2, 3, 4, 8, 9, 20, 40]

    print(triplet(nums1, 32))   # True
    print(triplet(nums1, 18))   # False
