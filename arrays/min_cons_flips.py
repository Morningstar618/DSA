"""
Find the minimum number of consecutive flips in an array
such that afterwards all the elements are the same.

i/p: [1, 1, 0, 0, 0, 1]
o/p: From 2 to 4

i/p: [1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
o/p: From 1 to 3 & From 5 to 6

i/p: [1, 1, 1]
o/p: ""

i/p: [0, 1]
o/p: From 0 to 0 OR From 1 to 1
"""

def flips(nums: list):
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] != nums[0]:
                print(f"From {i} to ", end='')
            else:
                print(f"{i - 1}")

    if nums[len(nums) - 1] != nums[0]:
        print(f"{len(nums) -1}")


if __name__ == '__main__':
    flips([1, 1, 0, 0, 0, 1])
    flips([1, 0, 0, 0, 1, 0, 0, 1, 1, 1])
    flips([1, 1, 1])
    flips([0, 1])
    flips([0, 0, 1, 1, 1, 0])
