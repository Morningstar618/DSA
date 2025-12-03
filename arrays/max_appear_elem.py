"""
Find the maximum appearing element in a range of arrays
defined via two arrays.

i/p: [1, 2, 4], [4, 5, 7]
ranges: [1, 2, 3, 4], [2, 3, 4, 5], [4, 5, 6, 7]
o/p: 4

NOTE: The above ranges are defined by first elem of the
first array and the second array.

Restraints:
    1. All elements will be less than 100 and greater than
       0.
    2. The element in the first array will be lower than
    its counterpart in the second array.

Approach: Use frequency array to map the start and end of 
each range. The start shall mark the index with the val 1
in the freq array and the end with -1. At last we calculate
the prefix sum and the index with the max sum will be our
element.
"""

def prefix_sum(nums: list):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]


def maxAppear(nums1: list, nums2: list) -> int:
    freq_arr = [0] * 100
    
    for i in range(len(nums1)):
        freq_arr[nums1[i]] = 1
        freq_arr[nums2[i] + 1] = -1

    prefix_sum(freq_arr)
    return freq_arr.index(max(freq_arr))


if __name__ == '__main__':
    res = maxAppear([1, 2, 4], [4, 5, 7])
    print(res)
