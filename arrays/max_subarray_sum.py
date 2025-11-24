"""
Find a max_sumay in the array with the highest sum

i/p: [2, 3, -8, 7, -1, 2, 3]
o/p: 11

i/p: [-3, -2, -1]
o/p: -1

Approach:
    1. Calculate the maximum sum possible for each index
       in the list. To calculate max, compare between that
       element and the sum of that element with the previous
       element's max.
    2. Store the above maximums for each index in an array
       and finally return the maximum value from that array.
"""

# Time -> O(n)  Space -> O(n)
def max_sum(nums: list) -> int:
    maxs = [nums[0]]
    
    for i in range(1, len(nums)):
        x = max(nums[i], nums[i] + maxs[i - 1])    
        maxs.append(x)

    return max(maxs)
        

if __name__ == '__main__':
    print(max_sum([2, 3, -8, 7, -1, 2, 3]))
    print(max_sum([-3, -2, -1]))
