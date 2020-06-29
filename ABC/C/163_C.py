N = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(1, N+1):
  d[i] = 0

for i in A:
  d[i] += 1

for i in range(1, N+1):
  print(d[i])