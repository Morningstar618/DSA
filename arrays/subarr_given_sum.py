"""
Find a subarray with a given sum where the array 
consists of +ve integers.

Approach: we use sliding window with variable size

Time - O(n), Space - O(1)

i/p: [1, 4, 20, 3, 10, 5], k = 33
o/p: yes

i/p: [1, 4, 0, 0, 3, 10, 5], k = 7
o/p: yes

i/p: [2, 4], k = 3
o/p: no
"""

def is_sub_sum(nums: list, k: int):
    s, e = [0, 0]
    curr = 0

    l_nums = len(nums)

    while e < l_nums:
        if curr == k:
            print("yes")
            return
    
        if curr < k:
            curr += nums[e]
            e += 1

        if curr > k:
            curr -= nums[s]
            s += 1

    print("no")
    return


if __name__ == '__main__':
    is_sub_sum([1, 4, 20, 3, 10, 5], 33)
    is_sub_sum([1, 4, 0, 0, 3, 10, 5], 7)
    is_sub_sum([2, 4], 3)


