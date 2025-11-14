"""
Find the second largest element in the array

------------------------------------------------------
Approach 1 O(n): use a var that shadows the largest var

Approach 2 O(2n): find the largest num in one run, then ignore
the num while looking for the second largest in the 
second run.
"""

# Time Complexity - O(n)
def res(nums: list) -> int:
    largest = nums[0]
    res = -1

    for num in nums:
        if num > largest:
            res = largest
            largest = num
        elif num > res and num < largest:
            res = num

    return res


if __name__ == '__main__':
    print(res([3, 2, 5, 4, 11, 9, 6, 8])) # 2
    print(res([10, 10, 10])) # -1
