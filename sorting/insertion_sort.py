"""
============= Insertion Sort =============
 - Theta(n^2) worst case (when array is reverse sorted)
 - Theta(n) in best case (happens when array is already sorted)
 - O(n^2) in general
 - In-place and stable
 - Used in practice for small arrays (TimSort and IntroSort)

Idea: We consider the first element as sorted. Then we move onto
the second element and then sort it with the first if required and
so on.
"""

def insert(arr: list):
    """Insertion Sort"""

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == '__main__':
    nums = [20, 5, 40, 60, 10, 30]
    insert(nums)
    print(nums)
