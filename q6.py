"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
from math import sqrt

c = 50
h = 30
l = list()
s = input()
g = (s.split(","))
# print(g[0])
# print(len(g))
for d in range(len(g)):
    q = int(sqrt((2 * c * int(g[d])) / h))
    l.append(str(q))
print(','.join(l))
