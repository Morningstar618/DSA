"""
Print the frequencies of every element in an array.

i/p: [10, 10, 10, 25, 30, 30]
o/p: 10 3, 25 1, 30 2
"""

def freq(nums: list):
    if nums == None:
        print("Empty list")
        return

    count = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            print(f"{nums[i - 1]} {count}")
            count = 0
        count += 1
    
    print(f"{nums[len(nums) - 1]} {count}")


if __name__ == '__main__':
    nums1 = [10, 10, 10, 25, 30, 30]
    freq(nums1)

    nums2 = [10]
    freq(nums2)
