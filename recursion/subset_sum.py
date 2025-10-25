'''------------------- Subset sum --------------------
In this problem, we are given an array `arr` with `n`
elements. Our goal is to find out the maximum number of
the subset of elements in the array that match the `sum`
when added together.
---------------------------------------------------'''


def sub_sum(arr: list, n: int, current_sum: int) -> int:
    if n == 0:
        return 1 if current_sum == 0 else 0

    return sub_sum(arr, n - 1, current_sum) + sub_sum(arr, n - 1, current_sum - arr[n - 1])


if __name__ == '__main__':
    print(sub_sum([10, 25, 5], 3, 25)) # 1
    print(sub_sum([4, 6, 3, 2, 5], 5, 8)) # 2
    print(sub_sum([4, 6, 1, 5], 4, 8)) # 0

