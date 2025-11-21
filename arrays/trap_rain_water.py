"""
Find the maximum amount of water we can trap.

i/p: [3, 0, 1, 2, 5]
o/p: 6

i/p: [3, 2, 1]
o/p: 0

Approach:
    Precompute the lmax and rmax for each column (element).
    Then find the minimum between lmax and rmax and subtract
    the value of column from it. Add the result cumulatively 
    to a var. Do it for all the columns between i=0 and 
    i=len(levels)-1.
"""

# Time - Theta(n)
def max_water(levels: list) -> int:
    res = 0
    length = len(levels)
    
    lmax = [None] * length
    rmax = [None] * length

    lmax[0] = levels[0]
    for i in range(1, length):
        lmax[i] = max(lmax[i - 1], levels[i])

    rmax[length - 1] = levels[length - 1]
    for i in range(length - 2, -1, -1):
        rmax[i] = max(rmax[i + 1], levels[i])

    for i in range(1, length):
        res += min(lmax[i], rmax[i]) - levels[i]

    return res


if __name__ == '__main__':
    print(max_water([3, 0, 1, 2, 5]))     # 6
    print(max_water([7, 2, 1, 0, 5, 6]))  # 16
    print(max_water([3, 2, 1]))           # 0
    print(max_water([1, 2, 3]))           # 0
