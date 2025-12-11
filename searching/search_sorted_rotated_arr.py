"""
Search 'k' in a sorted and rotated array.

Approach: Divide array in two ranges, one left
of Mid, and the other right. Check if 'k' lies
in either of them and adjust the start and end
values for binary search accordingly.

Time -> O(logn), Space -> O(1)

i/p: [20, 30, 50, 70, 5, 8], k = 5
o/p: 4
o/p: - 1 when 'k' not in array
"""

def search(nums: list, k: int) -> int:
    "Search 'k' in 'nums'"

    l = len(nums) - 1
    m = l // 2

    if nums[m] == k:
        return m

    s = 0 if nums[0] <= k < nums[m] else m + 1
    e = m - 1 if s == 0 else l

    while s <= e:
        m = int((s + e) // 2)
        if nums[m] == k:
            return m

        if nums[m] <= k:
            s = m + 1
        else:
            e = m - 1

    return -1


if __name__ == '__main__':
    nums1 = [20, 30, 50, 70, 5, 8]

    print(search(nums1, 5)) # 4
    print(search(nums1, 4)) # -1
    print(search(nums1, 20)) # 0
    print(search(nums1, 8)) # 5
