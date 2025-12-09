"""
Find Square root of 'x'.

i/p: 4
o/p: 2

i/p: 13
o/p: 3 (floor value)

Approach: Use binary search
Time -> O(logn), Space -> O(1)
"""

def root(x: int) -> int:
    "Func used to calc sq. root"

    s = 0
    e = x // 2
    ans = -1

    while s <= e:
        m = (s + e) // 2
        sq = m * m

        if sq == x:
            return m

        if sq > x:
            e = m - 1
        else:
            s = m + 1
            ans = m

    return ans


if __name__ == '__main__':
    print(root(4))  # 2
    print(root(13)) # 3
    print(root(3))  # 1
    print(root(1))  # 1
    print(root(0))  # 0
