def permute(s: str, i: int = 0):
    if i == len(s) - 1:
        print(s)
        return

    for j in range(i, len(s)):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        
        permute(''.join(lst), i + 1)

        lst[j], lst[i] = lst[i], lst[j]


if __name__ == '__main__':
    permute("ABC")
