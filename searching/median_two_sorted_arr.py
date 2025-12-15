"""
Find median of two sorted arrays.

i/p: [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]
o/p: 27.5

i/p: [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50]
o/p: 6

Approach: Make two sets from the two arrays such that
each set contains the following. 
    Firstly, we shall divide each array into two parts,
    represented by 'i1' and 'i2' which are the indexes
    that determine the start of the second half of the array.

    Set1 shall contain: {arr1[:i1], arr2[:i2]}
    Set2 shall contain: {arr1[i1:], arr2[i2:]}

We would have found the median when the maximum value in
Set1's arr1[:i1] is less than the minimum value in Set2's
arr2[i2:] AND the minimum value in Set2's arr1[i1:] is less
than the maximum value in Set1's arr2[:i2].

Also, in this approach we should ensure that the length of
arr1 is less than or equal to the length of arr2.

Time -> O(log<length of array1>), Space -> O(1)

NOTE: Good Problem
"""

def median(nums1: list, nums2: list) -> float:
    "Find median of 'nums1' and 'nums2'."

    l1 = len(nums1)
    l2 = len(nums2)

    s1 = 0
    e1 = l1

    while s1 <= e1:
        i1 = int((s1 + e1) / 2)
        i2 = int((l1 + l2 + 1) / 2 - i1)

        min1 = 10 * 10000 if i1 == l1 else nums1[i1]
        max1 = -10 * 10000 if i1 == 0 else nums1[i1 - 1]

        min2 = 10 * 10000 if i2 == l2 else nums2[i2]
        max2 = -10 * 10000 if i2 == 0 else nums2[i2 - 1]

        if max1 <= min2 and max2 <= min1:
            if (l1 + l2) % 2 == 0:
                return (max(max1, max2) + min(min1, min2)) / 2

            return max(max1, max2)

        if max1 > min2:
            e1 = i1 - 1
        else:
            s1 = i1 + 1

    return None


if __name__ == '__main__':
    x1 = [10, 20, 30, 40, 50]
    x2 = [5, 15, 25, 35, 45]
    print(median(x1, x2))       # 27.5

    x1 = [1, 2, 3, 4, 5, 6]
    x2 = [10, 20, 30, 40, 50]
    print(median(x1, x2))       # 6
