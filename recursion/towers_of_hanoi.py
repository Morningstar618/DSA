# No. of movements to make for a given 'n' value = 2^n -1
def TOH(n: int, A: str, B: str, C: str):
    if n == 1:
        print(f"Move disc 1 from {A} to {C}")
        return

    TOH(n - 1, A, C, B)
    print(f"Move disc {n} from {A} to {C}")
    TOH(n - 1, B, A, C)


if __name__ == '__main__':
    TOH(3, 'A', 'B', 'C')
