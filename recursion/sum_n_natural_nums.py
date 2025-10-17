def sum(n: int, _k: int = 0) -> int:
    if n == 0:
        return _k
    
    return sum(n - 1, _k + n)


if __name__ == '__main__':
    x = sum(5)
    print(x)
