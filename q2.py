"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

n = int(input("Enter your No.: "))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(n))

# f=n
# g=1
# f=(n**2)-n
# while n>1:
#     g=f*(n-1)
#     n=n-1
# print(f)

# fact(n)
