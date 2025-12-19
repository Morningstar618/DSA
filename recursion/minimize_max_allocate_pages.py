"""
Allocate minimum number of pages between
'k' students.

Rules:
    1. Minimize the pages allocated
    2. Only contiguous pages can be allocated

Fact: Every student must read atleast one book.

Approach: We divide the array with 'len(arr) - 1' 
cuts. We must choose from one of those arrays.
The chosen array should have the minimum maximum
page count.

i/p: [10, 20, 30, 40], k = 2
o/p: 60

The above array shall be divided with 3 cuts as follows:
    1. [10 | 20, 30, 40]
    2. [10, 20 | 30, 40]
    3. [10, 20, 30 | 40]

i/p: [10, 20, 30], k = 1
o/p: 60

i/p: [10, 5, 30, 1, 2, 5, 10, 10], k = 3
o/p: 30
"""

# Time -> O(n^k), Space -> O(n + k)
def min_pages(nums: list, n: int, k: int) -> int:
    """Caclculate minimum number of maximum
    pages."""

    if k == 1:
        return sum(nums[:n])

    if n == 1:
        return nums[0]

    res = 10 * 1000000

    for i in range(1, n):
        res = min(res, max(
            min_pages(nums, i, k - 1),
            sum(nums[i:n])))

    return res


if __name__ == '__main__':
    print(min_pages([10, 20, 30, 40], 4, 2))                # 60
    print(min_pages([10, 20, 30], 3, 1))                    # 60
    print(min_pages([10, 5, 30, 1, 2, 5, 10, 10], 8, 3))    # should return 30 but getting 45
