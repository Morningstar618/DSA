"""
Each element in the array represents the price of the stock on
a given day. Find the maximum profit by buying/selling the stock
on these respective days.

i/p: [1, 5, 3, 8, 12]
o/p: 13, i.e. (5-1) + (12-8)
"""

def profit(nums: list) -> int:
    profit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            profit += nums[i] - nums[i - 1]

    return profit


if __name__ == '__main__':
    res = profit([1, 5, 3, 8, 12])
    print(res)
