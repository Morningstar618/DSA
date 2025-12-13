"""
Find if there is a pair with sum 'k' in a
sorted array.

Approach: Two-pointer approach

Fact: Use the fact that the array is
sorted.

Time -> O(n), Space -> O(1)

i/p: [2, 5, 8, 12, 30], k = 17
o/p: True

i/p: [3, 8, 13, 18], k = 14
o/p: False
"""

def find_pair(nums: list, k: int) -> bool:
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


if __name__ == '__main__':
    nums1 = [2, 5, 8, 12, 30]
    print(find_pair(nums1, 17))     # True

    nums2 = [3, 8, 13, 18]
    print(find_pair(nums2, 14))     # False
