def operations(A, B):
  r1 = A+B
  r2 = A-B
  r3 = A*B

  if r1>=r2 and r1>=r3:
    return r1
  elif r2>=r1 and r2>=r3:
    return r2
  elif r3>=r1 and r3>=r2:
  	return r3

A = int(input())
B = int(input())
r = operations(A, B)
print(r)
