"""
Find the subarray within an array with the maximum sum.
Note that the array shall be treated as a circular array.

Approach:
    1. Find maximum sum of a subarray
    2. Find maximum sum of a circular subarray
        a. To find this, simply subtract the minimum sum
           of a subarray from the total sum of the array.
           What this does is it adds back the amount that
           was lost due to the lesser minimum values to
           the total sum of the array.
    3. Lastly, we take the maximum of the subarray and circular
       subarray sum we calculated in the first two steps.

Time Complexity -> Theta(n)

i/p: [5, -2, 3, 4]
o/p: 12
"""

def max_subarray_sum(nums: list) -> int:
    res = nums[0]
    curr = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], nums[i] + curr)
        res = max(res, curr)

    return res


def min_subarray_sum(nums: list) -> int:
    res = nums[0]
    curr = nums[0]

    for i in range(1, len(nums)):
        curr = min(nums[i], nums[i] + curr)
        res = min(res, curr)

    return res


def max_circular_sum(nums: list) -> int:
    max_subarr_sum = max_subarray_sum(nums)    
    # Return max -ve value
    if max_subarr_sum < 0:
        return max_subarr_sum

    min_subarr_sum = min_subarray_sum(nums)
    
    res = max(max_subarr_sum, sum(nums) - min_subarr_sum)
    return res


if __name__ == '__main__':
    print(max_circular_sum([5, -2, 3, 4]))        # 12
    print(max_circular_sum([8, -4, 3, -5, 4]))    # 12
    print(max_circular_sum([3, -4, 5, 6, -8, 7])) # 17
    print(max_circular_sum([-8, 4, 3, -5, -4]))   # 7
    print(max_circular_sum([-8, -4, -3, -5, -4])) # -3
    

