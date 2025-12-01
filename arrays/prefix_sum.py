"""
Find sum between the starting and ending prefix in an array.
Note that the end shall be included too in the sum.

Approach: Precompute the sum.

Time -> O(1), Space -> O(n)

i/p: [2, 8, 3, 9, 6, 5, 4]
o/p: 13 for s = 0 and e = 2
o/p: 20 for s = 1 and e = 3
o/p: 27 for s = 2 and e = 6
"""

# Precomputed sum for each index in the array
arr   = [2, 8, 3, 9, 6, 5, 4]
p_sum = [2, 10, 13, 22, 28, 33, 37]

def get_sum(s: int, e: int) -> int:
    if s == 0:
        return p_sum[e]
    else:
        return p_sum[e] - p_sum[s - 1]


if __name__ == '__main__':
    print(get_sum(0, 2))     # 13
    print(get_sum(1, 3))     # 20
    print(get_sum(2, 6))     # 27

