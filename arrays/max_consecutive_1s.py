"""
Find maximum consecutive 1s in a list

i/p: [0, 1, 1, 0, 1, 0]
o/p: 2

i/p: [1, 0, 1, 1, 1, 0, 1, 1]
o/p: 4

i/p: [1, 1, 1, 1]
o/p: 4

i/p: [0, 0, 0, 0]
o/p: 0
"""

def ones(nums: list) -> int:
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0

        max_count = max(max_count, count)

    return max_count


if __name__ == '__main__':
    print(ones([0, 1, 1, 0, 1, 0]))         # 2
    print(ones([1, 0, 1, 1, 1, 0, 1, 1]))   # 3
    print(ones([1, 1, 1, 1]))               # 4
    print(ones([0, 0, 0, 0]))               # 0
