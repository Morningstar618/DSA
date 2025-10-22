#---------------- Josephus Problem ------------------#
# There are `n` people standing in a circle. Starting
# from the first person, i.e. 0, we have to kill every
# k'th person. For example, if k = 2, Person 0 shall
# kill person 1. Like this we continue until there is
# a single person remaining and then we return that
# person.

def josephus(n: int, k: int) -> int:
    if n == 1:
        return 0

    # Understanding the below from the perspective
    # of base case where `0`, the first person shoots,
    # we return the survivor
    return (josephus(n - 1, k) + k) % n


if __name__ == '__main__':
    n = 4 # No. of people in the circle
    k = 2 # Kill every k'th person

    print("Survivor:", josephus(n, k))
