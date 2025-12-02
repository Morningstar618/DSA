"""
Find the equilibrium point in the array such that
the sum before that point and after that point is
the same.

Approach:
    1. Pre-compute prefix and suffix sum
       Time -> O(n), Space -> O(n)
    2. Precompute total sum and use left
       and right sum variables to find the
       equilibrium point.
       Time -> O(n), Space -> O(1)

i/p: [3, 4, 8, -9, 20, 6]
o/p: True

i/p: [4, 2, -2]
o/p: True

i/p: [4, 2, 2]
o/p: False
"""

def eq_point(nums: list) -> bool:
    l_sum = 0
    r_sum = sum(nums)

    for i in range(len(nums)):
        r_sum -= nums[i]

        if l_sum == r_sum:
            return True
        
        l_sum += nums[i]

    return False


if __name__ == '__main__':
    print(eq_point([3, 4, 8, -9, 20, 6]))   # True
    print(eq_point([4, 2, -2]))             # True
    print(eq_point([4, 2, 2]))              # False


