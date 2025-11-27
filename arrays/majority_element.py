"""
Find the majority element in an array i.e. it
should appear more the 'n > 2' times in the array
where 'n' is the length of the array. At the end
return any of the indexes of that element from the
array.

Approach:
    Here we use Moore's voting Algorithm to find the
    majority algorithm in an array. First we find a
    valid candidate then we verify whether its in
    majority or not.

Time -> O(n)    Space -> O(1)

i/p: [8, 3, 4, 8, 8]
o/p: 0 or 3, 4

i/p: [3, 7, 4, 7, 7, 5]
o/p: -1 (No majority)
"""

def majority(nums: list):
    res = 0
    count = 1

    # Find valid candidate
    for i in range(1, len(nums)):
        if nums[i] == nums[res]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            res = i
            count = 1

    # Verify if candidate is in majority
    count = 0

    for num in nums:
        if num == nums[res]:
            count += 1

    if count <= (len(nums) / 2):
        return -1

    return res


if __name__ == '__main__':
    print(majority([8, 3, 4, 8, 8]))                # 3
    print(majority([3, 7, 4, 7, 7, 5]))             # -1
    print(majority([20, 30, 40, 50, 50, 50, 50]))   # 3
    print(majority([3, 3, 4, 2, 4, 4, 2, 4, 4]))    # 4
    print(majority([1, 1, 2, 2]))                   # -1

