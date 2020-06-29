N, X, Y = map(int, input().split())
l = [0] * (N-1)

for i in range(1, N):
  for j in range(i+1, N+1):
    d = min(abs(j-i), abs(X-i)+1+abs(j-Y))
    l[d-1] += 1

for k in range(N-1):
  print(l[k])