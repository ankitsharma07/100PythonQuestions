x = int(input())
y = int(input())
z = int(input())

n = int(input())

arr = []
p = 0

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                arr.append([])
                arr[p] = [i, j, k]
                p+=1;

print(arr)


print('\nUsing list comprehensions the same thing is as easy as pie \n')

print [[i, j, k] for i in range(x+1) for j in range (y+1) for k in range (z+1) if ((i+j+k) != n)]
