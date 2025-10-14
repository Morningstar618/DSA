def printer(n: int):
    if (n == 0):
        return
    printer(n - 1) # Interchange this with the line below to print in the reverse order
    print(n)


printer(5)
