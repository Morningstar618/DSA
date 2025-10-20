def subsets(s: str, _curr: str = "", _i: int = 0):
    if _i == len(s):
        print(_curr)
        return

    subsets(s, _curr, _i + 1)
    subsets(s, _curr + s[_i], _i + 1)


if __name__ == '__main__':
    subsets("ABC")

