"""
Find the peak element in an array. The array
will be unsorted.

Approach: Binary search complementing with the
below fact.

Fact: If elem on left of mid is greater than or
equal to it, then peak lies on the left hand side
and vice-versa.

i/p: [5, 20, 40, 30, 20, 50, 50]
o/p: 40
"""

def peak(nums: list) -> int:
    "Find peak elem in 'nums'."
    l = len(nums)

    if l == 1:
        return nums[0]

    s = 0
    e = l - 1

    if nums[0] > nums[1]:
        return nums[0]

    if nums[e] > nums[e - 1]:
        return nums[e]

    while s <= e:
        m = int((s + e) // 2)

        if nums[m - 1] < nums[m] > nums[m + 1]:
            return nums[m]

        if nums[m - 1] > nums[m]:
            e = m - 1
        else:
            s = m + 1

    return -1


if __name__ == '__main__':
    nums1 = [5, 20, 40, 30, 20, 50, 50]

    print(peak(nums1))          # 40
    print(peak([1, 1, 1]))      # -1
    print(peak([10, 20, 10]))   # 20
    print(peak([10]))           # 10
    print(peak([22, 111]))      # 111
