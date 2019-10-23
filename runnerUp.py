# question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# @author : Ankit Sharma

n = int(input())

for i in range (0, n, 1):
    arr = int(input(i))

arr.sort()

print(arr)
