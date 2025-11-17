"""
Move the zeroes in an array to the end. The order of the 
elements should be maintained.

i/p: [8, 5, 0, 10, 0, 20]
o/p: [8, 5, 10, 20, 0, 0]

In this approach, we are using two pointers. The write_pos
simply points to the position we will be writing to. `i`
represents the data we will writing or rather swapping with.
Write_pos is incremented till the point there are non-zero
elements. Hence, it points to a zero. And when the next non-
zero element shows up, we swap.
"""

def move_zeroes(nums: list):
    write_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pos], nums[i] = nums[i], nums[write_pos]
            write_pos += 1


if __name__ == '__main__':
    nums1 = [8, 5, 0, 0, 10, 0, 20]
    move_zeroes(nums1)
    print(nums1)
