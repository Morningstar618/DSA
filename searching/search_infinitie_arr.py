"""
Find index of 'k' in an array of infinite size. 
Regarding the size, we assume its infinite. If
'k' is not found, return -1.

Approach: find a range where the value may lie, then
use binary search in that range

Time -> Theta(position), Space -> O(1)

i/p: [1, 10, 15, 20, 60, 100, 200, 500, 1000, 4000, 12000, 14000]
k = 100
o/p: 5
"""

def b_search(nums: list, k: int, s: int, e: int) -> int:
    """Perform binary search to find 'k' in 'nums' 
    between 's' and 'e'."""

    while s <= e:
        m = int((s + e) // 2)

        if nums[m] == k:
            return m

        if nums[m] < k:
            s = m + 1
        else:
            e = m - 1

    return -1


def search(nums: list, k: int) -> int:
    """Find index of 'k' in 'nums' which is
    assumed to be an inf array."""

    if nums[0] == k:
        return 0

    i = 1
    while nums[i] < k:
        i *= 2

    if nums[i] == k:
        return i

    return b_search(nums, k, (i / 2) + 1, i - 1)


if __name__ == '__main__':
    nums1 = [1, 10, 15, 20, 60, 100, 200, 500, 1000, 4000, 12000, 14000]

    print(search(nums1, 100))    # 5
    print(search(nums1, 111))    # -1
