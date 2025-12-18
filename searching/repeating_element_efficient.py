"""
Repeating Element O(n) Time, O(1)
Space solution with no changes to
original array.

NOTE: Good Problem!

Rules:
    1. All elements from 1 to max(arr) are present.
    2. 1 <= max(arr) <= n - 1

Fact: the first element of cycle will always be the repeating
element.

Approach: Use the 'Tortoise and Hare' Algorithm

i/p: [1, 3, 2, 4, 3, 3]
o/p: 3

i/p: [1, 1]
o/p: 1

i/p: [3, 4, 5, 1, 2, 5, 5]
o/p: 5

Additional Info:

This is **Floyd's Cycle Detection Algorithm**, also known as the **"Tortoise and Hare" algorithm**.

In this specific context, it's being used to solve the **"Find the Duplicate Number"** problem, 
where you have an array of n+1 integers where each integer is between 1 and n, and there's exactly 
one duplicate.

How it works:

1. Phase 1 (first while loop): The slow pointer moves one step at a time (`nums[slow]`), while the 
fast pointer moves two steps (`nums[nums[fast]]`). They treat the array indices and values as a 
linked list. Since there's a duplicate, there must be a cycle, and they'll eventually meet inside 
the cycle.

2. Phase 2 (second while loop): Reset one pointer to the start. Now move both pointers one step at 
a time. The point where they meet is the entrance to the cycle, which is the duplicate number.

Why it works: The duplicate value creates a cycle because multiple indices point to the same value. 
The mathematical proof relies on the fact that the distance from the start to the cycle entrance 
equals the distance from the meeting point to the cycle entrance (when traversing around the cycle).

This algorithm is elegant because it finds the duplicate in O(n) time and O(1) space, without 
modifying the array.
"""

def find(nums: list) -> int:
    "Find repeat elem in 'nums'."

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[fast]

        if slow == fast:
            break

    return slow


if __name__ == '__main__':
    # Cycle: 1 -> 3 -> 4 -> 6 -> 7 -> 3
    print(find([1, 3, 2, 4, 6, 5, 7, 3]))   # 3

    print(find([1, 3, 2, 4, 3, 3]))         # 3
    print(find([1, 1]))                     # 1

    # Cycle: 3 -> 1 -> 4 -> 2 -> 5 -> 5
    print(find([3, 4, 5, 1, 2, 5, 5]))      # 5
