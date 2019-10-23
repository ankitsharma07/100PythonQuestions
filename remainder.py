testCases = int(input())

def rem(x, y):
    r = x % y
    return r

for i in range(testCases):
    A = int(input())
    B = int(input())
    result = rem(A, B)
    print(result)
