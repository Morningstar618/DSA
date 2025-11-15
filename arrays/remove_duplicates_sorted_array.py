"""
Remove duplicates from sorted array

Key points:
    1. To modify a list in place, using reverse traversal as it will
       prevent index out of range errors.
    2. If you re-initialize the list (arr in the below func) inside the func,
       it will create a new list inside the func stack.
"""

def remove_duplicates(arr: list):
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == arr[i - 1]:
            # delete abstracted in python compared to other langs
            del arr[i]


if __name__ == '__main__':
    sorted_array = [10, 20, 20, 30, 30, 40, 50, 60, 60]
    remove_duplicates(sorted_array)
    print(sorted_array)

    sorted_array1 = [10, 10, 10]
    remove_duplicates(sorted_array1)
    print(sorted_array1)
