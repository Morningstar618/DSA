# Uses slicing: Only feasible for python
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


# Universal version
def is_palindrome_u(s: str, start: int, end: int) -> bool:
    if start >= end:
        return True

    # The string comparison before and operator acts as a circuit breaker
    return (s[start] == s[end]) and is_palindrome_u(s, start + 1, end - 1)


if __name__ == '__main__':
    s1 = "racecar"
    s2 = "race"

    print(is_palindrome(s1))
    print(is_palindrome(s2))

    print(is_palindrome_u(s1, 0, len(s1) - 1))
    print(is_palindrome_u(s2, 0, len(s2) - 1))
