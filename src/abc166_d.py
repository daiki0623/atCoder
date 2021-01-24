X = int(input())
A = 0
B = 0
while A**5 - B**5 == 0:
  A += 1
  if A**5 - X < 0:
    while A**5 - X <= B**5:
      if A**5 - X == B**5:
        break
      B -= 1
  elif A**5 - X > 0:
    while A**5 - X >= B**5:
      if A**5 - X == B**5:
        break
      B += 1
print(A, B)