def fact(n: int, k: int = 1) -> int:
    if n == 0 or n == 1:
        return k
    return fact(n - 1, k * n)


if __name__ == '__main__':
    x = fact(5)
    print(x)
