"""
Find the maximum sum of 'k' consecutive elements in an array.

Approach: Use sliding window technique

i/p: [1, 8, 30, -5, 20, 7], k = 3
o/p: 45

i/p: [5, -10, 6, 90, 3], k = 2
o/p: 96
"""

def max_sum(nums: list, k: int) -> int:
    x = sum(nums[:k])
    res = x

    i = 1
    while i < len(nums) -k + 1:
        # The below statement utilizes sliding window.
        # We could also use sum(nums[i:k-1]) but that would not be utilizing the technique
        x = x + nums[i + k - 1] - nums[i - 1]
        res = max(x, res)
        
        i += 1

    return res


if __name__ == '__main__':
    print(max_sum([1, 8, 30, -5, 20, 7], 3))
    print(max_sum([5, -10, 6, 90, 3], 2))

