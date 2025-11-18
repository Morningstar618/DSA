"""
Find leaders in an array

i/p: [7, 10, 4, 10, 6, 5, 2]
o/p: 10 6 5 2

Idea: traverse from right side
"""

# Using deque to store the output as insert
# at 0th index is O(1) operation instead of
# O(n) in list
from collections import deque

# -----------------------------------------
# Time - Theta(2n -i), Space O(n)
def leaders(nums: list) -> list:
    if nums == None:
        return None

    res = deque([])
    length = len(nums)

    res.appendleft(nums[length - 1])
    
    for i in range(length - 2, -1, -1):
        res.appendleft(nums[i])
        for j in range(i + 1, length):
            if nums[i] <= nums[j]:
                res.popleft()
                break
        
    return res


# Time - Theta(n), Space = O(1)
# Drawback - prints leaders in reverse order
# Fix - store leaders in array and print it in reverse
def efficient_leaders(nums: list):
    if nums == None:
        return None

    length = len(nums)
    curr_leader = nums[length - 1]
    print(curr_leader, end=' ')

    for i in range(length - 2, -1, -1):
        if curr_leader < nums[i]:
            curr_leader = nums[i]
            print(curr_leader, end=' ')


# -------------------------------------------
if __name__ == '__main__':
    nums1 = [7, 10, 4, 10, 6, 5, 2]
    efficient_leaders(nums1)

