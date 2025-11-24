"""
Find a max_sumay in the array with the highest sum

i/p: [2, 3, -8, 7, -1, 2, 3]
o/p: 11

i/p: [-3, -2, -1]
o/p: -1
"""

# Time -> O(n)  Space -> O(1)
def max_sum(nums: list) -> int:
    res = nums[0]
    max_ending = nums[0]
    
    for i in range(1, len(nums)):
        max_ending = max(nums[i], nums[i] + max_ending)    
        res = max(max_ending, res)

    return res
        

if __name__ == '__main__':
    print(max_sum([2, 3, -8, 7, -1, 2, 3]))
    print(max_sum([-3, -2, -1]))
