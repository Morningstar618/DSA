"""
Binary search: iterative

i/p: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
o/p: 2 (index of 3)

i/p: [1, 2, 3, 4], k = 5
o/p: -1
"""

# Time O(logn)
def b_search(nums: list, k: int) -> int:
    s = 0
    e = len(nums) - 1 # Subtracting -1 crucial to prevent index errors
    m = int((s + e) / 2 )

    while s <= e:
        if nums[m] == k:
            return m

        if nums[m] < k:
            s = m + 1

        if nums[m] > k:
            e = m - 1

        m = int((s + e) / 2)

    return -1


if __name__ == '__main__':
    print(b_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))     # 2
    print(b_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))    # -1

