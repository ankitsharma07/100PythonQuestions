"""
Read an integer N.
Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.
"""

a = int(input())
for i in range(1,a+1):
    print(i, end = '')