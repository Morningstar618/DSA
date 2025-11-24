"""
Find the longest consecutive length of subarray such that
if the current element is odd, the next one is even and
vice-versa.

i/p: [10, 12, 14, 7, 8]
o/p: 3

i/p: [7, 10, 13, 14]
o/p: 4

i/p: [10, 12, 8, 4]
o/p: 1
"""

# Time - Theta(n)
def max_even_odd(nums: list) -> int:
    count = 1
    res = 1

    for i in range(1, len(nums)):
        prev = nums[i - 1] % 2
        curr = nums[i] % 2
        if prev != curr:
            count += 1
        else:
            count = 1

        res = max(res, count)

    return res


if __name__ == '__main__':
    print(max_even_odd([10, 12, 14, 7, 8])) # 3
    print(max_even_odd([7, 10, 13, 14]))    # 4
    print(max_even_odd([10, 12, 8, 4]))     # 0
