"""
Find the maximum repeating element in an array.

Rules:
    1. Array size >= 2
    2. Only one element repeats (Any number of times)
    3. All the elements from 0 to max(arr) are present.
    Therefore, 0 <= max(arr) <= n-2
    4. No modifications allowed to the original array.

Approach: Use a bool arr of len(i/p)

Time -> O(n), Space -> O(n)

i/p: [0, 2, 1, 3, 2, 2]
o/p: 2

i/p: [1, 2, 3, 0, 3, 4, 5]
o/p: 3

i/p: [0, 0]
o/p: 0
"""

def find(nums: list) -> int:
    "Find max repeat elem in 'nums'."

    l = len(nums)
    temp = [False] * l

    for i in range(l):
        if temp[nums[i]] is True:
            return nums[i]
        temp[nums[i]] = True

    return None


if __name__ == '__main__':
    print(find([0, 2, 1, 3, 2, 2]))     # 2
    print(find([1, 2, 3, 0, 3, 4, 5]))  # 3
    print(find([0, 0]))                 # 0
