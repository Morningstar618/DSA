"""
Find weighted prefix sum in an array.

i/p: [2, 3, 5, 4, 6, 1]
o/p:
    getWSum(0, 2) = 23 -> 1 * arr[0] + 2 * arr[1] + 3 * arr[2]
    getWSum(2, 3) = 13 -> 1 * arr[2] + 2 * arr[3]

Time - O(1), Space - O(2n)

Approach:
    getWSum = sum up the expression '(i - l + 1) * arr[i]' for each value from
                'i = l' upto 'r'.
              => (i * arr[i]) - ((l - 1) * arr[i])
              => the latter part of the above equation is 'l - 1' multiplied with the
                 calculated prefix sum.
    
    In short, we subtract 'l - 1' times prefix sum from the precomputed weighted sum i.e.
    'i * arr[i]' to get the answer in constant time. For this we will require two arrays,
    one for precomputed sum, and the other for precomputed weighted sum.
"""

def pSum(nums: list) -> list:
    """Precompute sum for array"""
    res = [nums[0]]

    for i in range(1, len(nums)):
        x = nums[i] + res[i - 1]
        res.append(x)

    return res

def pWSum(nums: list) -> list:
    """Precompute weighted sum for array"""
    res = [nums[0]]

    for i in range(1, len(nums)):
        x = (i + 1) * arr[i] + res[i - 1]
        res.append(x)

    return res

# Defining array, precompute and precompute weighted sum
arr = [2, 3, 5, 4, 6, 1]
p_sum = pSum(arr)   # [2, 5, 10, 14, 20, 21]
pw_sum = pWSum(arr) # [2, 8, 23, 39, 69, 75]

def getWSum(l: int, r: int) -> list:
    """
    Calculate weighted sum.

    min 'l' val = 0
    max 'r' val = 5

    above values are as per the size of the
    list 'arr'
    """
    if l == 0:
        return pw_sum[r]
    else:
        return pw_sum[r] - pw_sum[l - 1] - l * (p_sum[r] - p_sum[l - 1])
                                         # This is the adjustment for indices
                                         # when l > 0


if __name__ == '__main__':
    print(getWSum(0, 2))    # 23
    print(getWSum(2, 3))    # 13
    print(getWSum(3, 5))    # 19

