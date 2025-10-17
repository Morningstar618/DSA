## Tail recursion takes less time than normal recursion

# print(n)          | func(n - 1)
# func(n - 1)       | print(n)

# Note: the 1st column takes less time. This is so on modern compilers.
# The reason for this is that in tail recursion we don't need to save the
# state of the caller, whereas in non-tail recursive functions, we need to
# save the state. Modern compilers do Tail-call elimination, to optimize
# the code.

# Tail recursion is also the reason why quick sort is faster than merge sort.

----------------------------------------------------------------------------------------

## NOTES: 

# These are the cases that cannot be broken down into further smaller problems.

# At any given moment, there will be n+1 functional stacks for a recursive f(n) function.

# Some optimized C and some other compilers don't stack the function calls together when 
# it's a tail recursive function.


