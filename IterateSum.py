"""
Given a range of the first 10 numbers, Iterate from the 
start number to the end number, and In each iteration print 
the sum of the current number and previous number.
"""

l = []

for i in range(10):
    l.append(int(input("Enter a No: ")))

for i in range(11):
    if i+1==11:
        break
    else:
        print("current Number", l[i], "Previous Number", l[i-1],"sum: ", l[i]+l[i-1])