"""
Given a string, display only those characters which are present
at an even index number.
"""

str = input()

for i in range(len(str)):
    a = i%2
    if a != 0:
        print(str[i], end="")