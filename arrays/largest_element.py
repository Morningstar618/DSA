"""
Find the largest element in an array
"""

def maxx(nums: list) -> int:
    max = -10 * 1000
    for num in nums:
        if num > max:
            max = num
    return max


if __name__ == '__main__':
    print(maxx([12, 22, 96, 50, 32]))
